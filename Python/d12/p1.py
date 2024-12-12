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
    height = len(grid)
    width = len(grid[0])
    return {"grid": grid, "height": height, "width": width}


def solve(grid_state):
    visited = set()
    res = 0
    for y, row in enumerate(grid_state["grid"]):
        for x, cell in enumerate(row):
            num_of_fences, num_of_areas = count_area_and_fences(
                grid_state, y, x, visited, cell
            )
            res += num_of_fences * num_of_areas
    return res


def check_bounds(y, x, height, width):
    return 0 <= y < height and 0 <= x < width


def count_area_and_fences(grid_state, y, x, visited, target):
    num_of_fences = 0
    num_of_areas = 0
    if not check_bounds(y, x, grid_state["height"], grid_state["width"]):
        return num_of_fences + 1, num_of_areas
    if grid_state["grid"][y][x] != target:
        return num_of_fences + 1, num_of_areas
    if (y, x) in visited:
        return num_of_fences, num_of_areas
    visited.add((y, x))
    num_of_areas += 1
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        n_num_of_fences, n_num_of_areas = count_area_and_fences(
            grid_state, y + direction[0], x + direction[1], visited, target
        )
        num_of_fences += n_num_of_fences
        num_of_areas += n_num_of_areas
    return num_of_fences, num_of_areas


def main():
    grid_state = generate_grid("Python/d12/input.txt")
    res = solve(grid_state)
    print(res)


if __name__ == "__main__":
    main()
