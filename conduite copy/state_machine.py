from typing import Dict


def update_state(current_state: str, action: str, config: Dict) -> str:
    if current_state == "END":
        return "END"

    return config["transitions"].get(action, current_state)