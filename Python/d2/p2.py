def parse_file(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def map_string_to_int(line_str):
    return list(map(int, line_str))


def check_within_bounds(prev, curr, is_inc):
    if curr == prev:
        return False
    if is_inc and prev < curr and curr - prev <= 3:
        return True
    if not is_inc and prev > curr and prev - curr <= 3:
        return True
    return False


def check_for_truncated(line_list):
    for i in range(len(line_list)):
        new_line_list = line_list[:i] + line_list[i + 1 :]
        if len(new_line_list) < 2:
            continue

        is_inc = new_line_list[0] < new_line_list[1]

        valid = True
        for j in range(1, len(new_line_list)):
            if not check_within_bounds(new_line_list[j - 1], new_line_list[j], is_inc):
                valid = False
                break

        if valid:
            return True

    return False


def solve(path):
    res = 0
    for line in parse_file(path):
        line_list = map_string_to_int(line.split())
        if len(line_list) < 2:
            continue

        is_inc = line_list[0] < line_list[1]
        is_unsafe = False

        for i in range(1, len(line_list)):
            if not check_within_bounds(line_list[i - 1], line_list[i], is_inc):
                is_unsafe = not check_for_truncated(line_list)
                break

        if not is_unsafe:
            res += 1
    return res


def main():
    # res = solve("Python/d2/small.txt")
    res = solve("Python/d2/input.txt")
    print(f"Solution: {res}")


if __name__ == "__main__":
    main()
