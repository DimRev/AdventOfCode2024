def parse_file(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def apply_rules(line_list):
    new_line_list = []
    for i, num in enumerate(line_list):
        if num == 0:
            new_line_list.append(1)
        elif len(str(num)) > 1 and len(str(num)) % 2 == 0:
            num_str = str(num)
            m = len(num_str) // 2
            new_line_list.append(int(num_str[:m]))
            new_line_list.append(int(num_str[m:]))
        else:
            new_line_list.append(num * 2024)
    return new_line_list


def solve(path, n):
    for line in parse_file(path):
        line_list = list(map(lambda x: int(x), line.split()))
        for i in range(n):
            # print(f"{i} = {str.join(' ', list(map(lambda x: str(x),line_list)))}")
            line_list = apply_rules(line_list)
        # print(f"{i + 1} = {str.join(' ', list(map(lambda x: str(x),line_list)))}")
        print(len(line_list))


def main():
    # solve("Python/d11/small.txt", 6)
    solve("Python/d11/input.txt", 25)


if __name__ == "__main__":
    main()
