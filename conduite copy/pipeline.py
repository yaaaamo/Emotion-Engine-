import json
from typing import Dict, Tuple

from oracle import process_json_request
from messages import build_message
from state_machine import update_state


def process_turn(
    data: Dict,
    current_state: str,
    last_action: str,
    config: Dict
) -> Tuple[Dict, str, str]:
    user_text = data.get("user_text", "")

    payload = {
        "user_text": user_text,
        "current_system_action": last_action
    }

    raw_response = process_json_request(json.dumps(payload))
    oracle_result = json.loads(raw_response)

    action = oracle_result.get("next_system_action", config["invalid_action"])
    reaction = oracle_result.get("mapped_vad_state", "stays_negative")
    vad_scores = oracle_result.get("vad_scores", {})

    next_state = update_state(current_state, action, config)
    message = build_message(action, next_state, reaction, config)

    output = {
        "action": action,
        "message": message,
        "next_state": next_state,
        "vad_scores": vad_scores,
        "mapped_vad_state": reaction,
    }

    return output, next_state, action


def process_line(
    line: str,
    current_state: str,
    last_action: str,
    config: Dict
) -> Tuple[Dict, str, str]:
    try:
        data = json.loads(line)
    except json.JSONDecodeError:
        action = config["invalid_action"]
        next_state = update_state(current_state, action, config)
        message = build_message(action, next_state, "stays_negative", config)

        return {
            "action": action,
            "message": message,
            "next_state": next_state,
        }, next_state, action

    return process_turn(data, current_state, last_action, config)