from typing import Dict


def build_message(action: str, next_state: str, reaction: str, config: Dict) -> str:
    if action == "offer_support":
        if reaction == "stays_negative":
            message = "I'm sorry you're still feeling this way. I'm here to support you and help."
        elif reaction == "opens_up":
            message = "Thank you for sharing that. I'm here to support you."
        else:
            message = "I'm here with you, and I want to help."

    elif action == "de_escalate":
        if reaction == "rejects_help":
            message = "I hear that this feels intense. Let's pause and try to stay calm for a moment."
        elif reaction == "stays_negative":
            message = "This sounds difficult. Let's slow things down and take it one step at a time."
        else:
            message = "Let's pause for a moment and keep things calm."

    elif action == "slow_down":
        if reaction == "stays_negative":
            message = "Let's slow down and go through this calmly, one piece at a time."
        elif reaction == "rejects_help":
            message = "Let's take this slowly and avoid rushing right now."
        else:
            message = "Let's slow down and take this step by step."

    elif action == "ask_clarification":
        if next_state == "DEESCALATE":
            message = "I want to understand better while keeping this calm. Can you tell me a bit more?"
        elif reaction == "opens_up":
            message = "Can you tell me a little more about what you're feeling?"
        else:
            message = "Could you clarify what you mean?"

    elif action == "suggest_pause":
        message = "Let's take a short pause and breathe for a moment."

    elif action == "continue":
        if reaction == "opens_up":
            message = "That helps me understand. Please continue."
        else:
            message = "Please go on. I'm listening."

    elif action == "acknowledge":
        message = "I understand."

    elif action == "encourage":
        if reaction == "opens_up":
            message = "You're expressing this clearly. Keep going."
        else:
            message = "You're doing well. Keep going."

    else:
        message = config["invalid_message"]

    if next_state == "SUPPORT":
        if not any(word in message.lower() for word in ["help", "support", "here"]):
            message = "I'm here to support you and help if I can."

    if next_state == "DEESCALATE":
        if not any(word in message.lower() for word in ["calm", "pause", "slow"]):
            message = "Let's pause for a moment and try to stay calm."

    return message if message.strip() else config["invalid_message"]