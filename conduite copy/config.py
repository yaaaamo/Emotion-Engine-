CONFIG = {
    "actions": {
        "continue",
        "slow_down",
        "ask_clarification",
        "offer_support",
        "de_escalate",
        "suggest_pause",
        "acknowledge",
        "encourage",
    },
    "states": {
        "START",
        "SUPPORT",
        "DEESCALATE",
        "END",
    },
    "initial_state": "START",
    "default_current_action": "acknowledge",
    "invalid_action": "ask_clarification",
    "invalid_message": "Could you tell me a bit more about what you're feeling?",
    "transitions": {
        "offer_support": "SUPPORT",
        "de_escalate": "DEESCALATE",
        "suggest_pause": "END",
    },
}