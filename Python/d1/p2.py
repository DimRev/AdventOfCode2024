def parse_file(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def generate_sorted_lists(path):
    curr_num = ""
    dict_a = {}
    list_b = []
    for line in parse_file(path):
        for char in line:
            if not char.isspace():
                curr_num += str(char)
            else:
                if curr_num != "":
                    if curr_num not in dict_a:
                        dict_a[curr_num] = 1
                    else:
                        dict_a[curr_num] += 1
                    curr_num = ""
        list_b = binary_insert(list_b, int(curr_num))
        curr_num = ""
    return dict_a, list_b


def binary_insert(curr_list, num):
    if len(curr_list) == 0:
        return [num]
    if num < curr_list[0]:
        return [num] + curr_list
    if num > curr_list[-1]:
        return curr_list + [num]

    s = 0
    e = len(curr_list) - 1
    while s <= e:
        m = (s + e) // 2

        if m + 1 < len(curr_list) and curr_list[m] < num < curr_list[m + 1]:
            return curr_list[: m + 1] + [num] + curr_list[m + 1 :]

        if num > curr_list[m]:
            s = m + 1
        else:
            e = m - 1

    # fallback
    return curr_list[:s] + [num] + curr_list[s:]


def count_distance(list_a, list_b):
    i = 0
    dist = 0
    while i < len(list_a):
        dist += abs(list_a[i] - list_b[i])
        i += 1
    return dist


def similarity_score(dict_a, list_b):
    total = 0
    for num in list_b:
        if str(num) in dict_a:
            total += num * dict_a[str(num)]
    return total


def main():
    # dict_a, list_b = generate_sorted_lists("d1/small.txt")
    dict_a, list_b = generate_sorted_lists("Python/d1/input.txt")
    score = similarity_score(dict_a, list_b)
    print(f"Similarity score: {score}")


if __name__ == "__main__":
    main()
