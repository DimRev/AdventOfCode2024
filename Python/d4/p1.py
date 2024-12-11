DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
WORD = ["X", "M", "A", "S"]


def parse_file(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            yield line


def generate_grid(path):
    grid = []
    line_list = []
    for line in parse_file(path):
        for ch in line:
            line_list.append(ch)
        grid.append(line_list)
        line_list = []
    HEIGHT = len(grid)
    WIDTH = len(grid[0])
    return grid, HEIGHT, WIDTH


def solve(grid, HEIGHT, WIDTH):
    count = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "X":
                count += count_all_directions(grid, y, x, HEIGHT, WIDTH)
    return count


def check_bounds(y, x, HEIGHT, WIDTH):
    return 0 <= y < HEIGHT and 0 <= x < WIDTH


def count_all_directions(grid, y, x, HEIGHT, WIDTH):
    count = 0
    for direction in DIRECTIONS:
        if is_valid_direction(grid, y, x, HEIGHT, WIDTH, direction, 0):
            count += 1
    return count


def is_valid_direction(grid, y, x, HEIGHT, WIDTH, direction, i):
    if not check_bounds(y, x, HEIGHT, WIDTH):
        return False
    if not grid[y][x] == WORD[i]:
        return False
    if i == len(WORD) - 1:
        # return True
        return True
    dy, dx = direction
    return is_valid_direction(grid, y + dy, x + dx, HEIGHT, WIDTH, direction, i + 1)


def main():
    # grid, HEIGHT, WIDTH = generate_grid("Python/d4/small.txt")
    grid, HEIGHT, WIDTH = generate_grid("Python/d4/input.txt")
    count = solve(grid, HEIGHT, WIDTH)
    print(count)


if __name__ == "__main__":
    main()
