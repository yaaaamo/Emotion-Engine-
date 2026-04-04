import sys
import json

from config import CONFIG
from pipeline import process_line


def main() -> None:
    state = CONFIG["initial_state"]
    last_action = CONFIG["default_current_action"]

    for raw_line in sys.stdin:
        line = raw_line.strip()
        if not line:
            continue

        output, state, last_action = process_line(line, state, last_action, CONFIG)
        print(json.dumps(output, ensure_ascii=False))


if __name__ == "__main__":
    main()