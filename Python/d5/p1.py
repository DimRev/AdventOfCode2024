def parse_file(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            yield line


def parse(path):
    is_rules = True
    rules_dict = {}
    result = 0
    for line in parse_file(path):
        if line == "":
            is_rules = False
        elif is_rules:
            add_to_rules_dict(rules_dict, line)
        else:
            if check_pages(rules_dict, line):
                pages_list = list(map(int, line.split(",")))

                result += pages_list[len(pages_list) // 2]
    return result


def add_to_rules_dict(rules_dict, rule):
    before, after = rule.split("|")
    if before not in rules_dict:
        rules_dict[before] = {"before": [], "after": []}
    if after not in rules_dict:
        rules_dict[after] = {"before": [], "after": []}
    rules_dict[before]["after"].append(after)
    rules_dict[after]["before"].append(before)


def check_pages(rules_dict, pages):
    pages_list = pages.split(",")
    for i, page in enumerate(pages_list):
        if page in rules_dict:
            if any(
                before_page in pages_list[i + 1 :]
                for before_page in rules_dict[page]["before"]
            ):
                return False
    return True


def main():
    # result = parse("Python/d5/small.txt")
    result = parse("Python/d5/input.txt")
    print(result)


if __name__ == "__main__":
    main()
