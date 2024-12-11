import functools


def parse_file(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


@functools.lru_cache(maxsize=None)
def single_blink_stone(value):
    text = str(value)
    if value == 0:
        # Rule 1: 0 -> 1
        return (1, None)
    elif len(text) > 1 and (len(text) % 2 == 0):
        # Rule 2: Split an even-length number
        mid = len(text) // 2
        left_stone = int(text[:mid])
        right_stone = int(text[mid:])
        return (left_stone, right_stone)
    else:
        # Rule 3: Multiply by 2024
        return (value * 2024, None)


@functools.lru_cache(maxsize=None)
def count_stone_blinks(stone, depth):
    left_stone, right_stone = single_blink_stone(stone)
    if depth == 1:
        # At the last iteration, just count how many stones result
        return 1 if right_stone is None else 2
    else:
        # Continue blinking for the next iteration
        count = count_stone_blinks(left_stone, depth - 1)
        if right_stone is not None:
            count += count_stone_blinks(right_stone, depth - 1)
        return count


def solve(path, n):
    for line in parse_file(path):
        if not line:
            continue
        initial_stones = list(map(int, line.split()))
        total_count = 0
        for stone in initial_stones:
            total_count += count_stone_blinks(stone, n)
        print(total_count)


def main():
    solve("Python/d11/input.txt", 75)


if __name__ == "__main__":
    main()
