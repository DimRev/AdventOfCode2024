from collections import defaultdict, deque


def parse_file(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def parse(path):
    rules_dict, result, is_rules = {}, 0, True
    for line in parse_file(path):
        if line == "":
            is_rules = False
        elif is_rules:
            add_to_rules_dict(rules_dict, line)
        else:
            if not check_pages(rules_dict, line):
                pages_list = list(map(int, line.split(",")))
                result += reorder_pages(rules_dict, pages_list)[len(pages_list) // 2]
    return result


def add_to_rules_dict(rules_dict, rule):
    before, after = rule.split("|")
    rules_dict.setdefault(before, {"before": [], "after": []})
    rules_dict.setdefault(after, {"before": [], "after": []})
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


def reorder_pages(rules_dict, pages_list):
    in_degree, graph = defaultdict(int), defaultdict(list)
    for page in pages_list:
        if str(page) in rules_dict:
            for after_page in rules_dict[str(page)]["after"]:
                after_page_int = int(after_page)
                if after_page_int in pages_list:
                    graph[page].append(after_page_int)
                    in_degree[after_page_int] += 1
    for page in pages_list:
        in_degree.setdefault(page, 0)
    queue = deque(sorted([page for page in pages_list if in_degree[page] == 0]))
    ordered_pages = []
    while queue:
        current = queue.popleft()
        ordered_pages.append(current)
        for neighbor in sorted(graph[current]):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return ordered_pages + [page for page in pages_list if page not in ordered_pages]


def main():
    print(parse("Python/d5/input.txt"))


if __name__ == "__main__":
    main()
