Emotion Engine 
Members: Yagmur AYDEMIR, Meriem BACHI
Group Name : InsideOut
Parcours : GL

1. Overview

This project implements a simple multi-turn chatbot system based on an emotion–reaction engine.

The system processes user input in three steps:

1. It receives a text input from the user.
2. It queries an oracle that returns an emotion and a confidence level.
3. It applies a dialogue policy to determine the appropriate action and message.

The system also maintains an internal dialogue state across multiple turns.

---

2. Architecture

The project is modular and divided into the following components:

* main.py
  Handles input/output. Reads JSON lines from STDIN and prints JSON responses to STDOUT.

* pipeline.py
  Coordinates one dialogue turn: oracle → policy → state update → message.

* oracle.py
  Simulates an external oracle using keyword matching to detect:
  emotion ∈ {joy, sadness, anger, fear, disgust, surprise}
  confidence ∈ {low, medium, high}

* policy.py
  Implements the dialogue logic:
  (emotion, confidence) → action

* state_machine.py
  Handles state transitions:
  START, SUPPORT, DEESCALATE, END

* messages.py
  Generates the final response message from the selected action.

* config.py
  Contains all configurable data:

  * emotions
  * confidence levels
  * actions
  * policy rules
  * messages
  * state transitions

---

3. Dialogue Logic

The system follows a rule-based mapping:

(emotion, confidence) → action

Examples:

* sadness + high → offer_support
* anger + high → de_escalate
* fear + high → suggest_pause

Invalid inputs result in:
action = ask_clarification

---

4. State Machine

The system maintains an internal state:

START → SUPPORT → DEESCALATE → END

Transition rules:

* offer_support → SUPPORT
* de_escalate → DEESCALATE
* suggest_pause → END
* otherwise → state remains unchanged

Important:
END is an absorbing state (once reached, it never changes).

---

5. Input Format

The program reads JSON objects line by line from STDIN.

Each input must contain:

* "user_text" (string)

Optional:

* "emotion" (string)
* "confidence" (string)

Example:

{"user_text":"I failed again."}
{"user_text":"Whatever.","emotion":"anger","confidence":"medium"}

---

6. Output Format

For each input line, the program outputs one JSON object:

{"action":"...","message":"...","next_state":"..."}

Constraints:

* message is always non-empty
* SUPPORT messages contain: help / support / here
* DEESCALATE messages contain: calm / pause / slow

---

7. How to Run

Run the program using:

python3 main.py < input.txt

---

8. Example Input

{"user_text":"Hi, I feel good today, really good."}
{"user_text":"Wow, that was unexpected."}
{"user_text":"But now I failed my exam and I feel sad and down."}
{"user_text":"I feel lonely and hurt."}
{"user_text":"Whatever, this is stupid."}
{"user_text":"I am really angry and furious."}
{"user_text":"Now I feel anxious and worried about everything."}
{"user_text":"I am scared and nervous."}
{"user_text":"This situation is disgusting and awful."}
{"user_text":"I love this, it’s awesome and wonderful."}
{"user_text":"I feel happy."}
{"user_text":"Something happened."}

Example Output :

{"action": "continue", "message": "Please continue.", "next_state": "START"}
{"action": "ask_clarification", "message": "Could you clarify what you mean?", "next_state": "START"}
{"action": "offer_support", "message": "I am here to support and help you.", "next_state": "SUPPORT"}
{"action": "offer_support", "message": "I am here to support and help you.", "next_state": "SUPPORT"}
{"action": "de_escalate", "message": "Let us stay calm and pause for a moment.", "next_state": "DEESCALATE"}
{"action": "de_escalate", "message": "Let us stay calm and pause for a moment.", "next_state": "DEESCALATE"}
{"action": "suggest_pause", "message": "Let us pause for a moment and breathe.", "next_state": "END"}
{"action": "suggest_pause", "message": "Let us pause for a moment and breathe.", "next_state": "END"}
{"action": "de_escalate", "message": "Let us stay calm and pause for a moment.", "next_state": "END"}
{"action": "continue", "message": "Please continue.", "next_state": "END"}
{"action": "continue", "message": "Please continue.", "next_state": "END"}
{"action": "ask_clarification", "message": "Could you clarify what you mean?", "next_state": "END"}

---

9. Design Choices

* The system is modular to allow easy modification.
* All labels and rules are stored in config.py.
* The oracle is implemented as a simple keyword-based function.
* The architecture allows replacing the oracle with a more advanced external system in the future.

---

10. Extensibility

The system is designed to be easily adaptable:

* New emotions can be added in config.py.
* New confidence levels can be introduced.
* Dialogue policies can be modified by updating the policy table.
* State transitions can be changed independently.

This ensures flexibility for future extensions of the project.

---
