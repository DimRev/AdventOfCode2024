def parse_file(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield from line.strip()


def check_is_mul(buffer, char):
    is_mul = False
    if char == "m" and len(buffer) == 0:
        buffer += char
    elif char == "u" and peek(buffer) == "m":
        buffer += char
    elif char == "l" and peek(buffer) == "u":
        buffer += char
    elif char == "(" and peek(buffer) == "l":
        buffer = ""
        is_mul = True
    else:
        buffer = ""

    return buffer, is_mul


def check_is_digit(buffer, char, state):
    if char.isdigit():
        buffer += char
    elif char == "," and len(buffer) > 0:
        state["val_x"] = int(buffer)
        buffer = ""
    elif char == ")" and len(buffer) > 0:
        state["val_y"] = int(buffer)
        buffer = ""
        state["is_mul"] = False
        state["res"] += state["val_x"] * state["val_y"]
        state["val_x"] = -1
        state["val_y"] = -1
    else:
        buffer = ""
        state["is_mul"] = False
    return buffer, state


def check_enable(buffer, char, state):
    if char == "d" and len(buffer) == 0:
        state["is_checking_do"] = True
        buffer += char
    elif char == "o" and peek(buffer) == "d":
        buffer += char
    # Do path
    elif char == "(" and peek(buffer) == "o":
        buffer += char
    elif char == ")" and buffer == "do(":
        state["is_enabled"] = True
        state["is_checking_do"] = False
        buffer = ""

    # Don't path
    elif char == "n" and peek(buffer) == "o":
        buffer += char
    elif char == "'" and peek(buffer) == "n":
        buffer += char
    elif char == "t" and peek(buffer) == "'":
        buffer += char
    elif char == "(" and peek(buffer) == "t":
        buffer += char
    elif char == ")" and peek(buffer) == "(":
        state["is_checking_do"] = False
        state["is_enabled"] = False
        buffer = ""
    else:
        state["is_checking_do"] = False

    return buffer, state


def solve(path):
    state = {
        "is_mul": False,
        "is_checking_do": False,
        "is_enabled": True,
        "val_x": -1,
        "val_y": -1,
        "res": 0,
    }
    buffer = ""

    for char in parse_file(path):
        buffer, state = check_enable(buffer, char, state)
        if state["is_enabled"] and not state["is_checking_do"]:
            if not state["is_mul"]:
                buffer, state["is_mul"] = check_is_mul(buffer, char)
            else:
                buffer, state = check_is_digit(buffer, char, state)
    print(f"res {state['res']}")


def peek(buffer):
    if len(buffer) == 0:
        return ""
    return buffer[-1]


def main():
    # solve("Python/d3/small2.txt")
    solve("Python/d3/input.txt")


if __name__ == "__main__":
    main()
