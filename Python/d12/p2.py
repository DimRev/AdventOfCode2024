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


def is_valid(grid_state, y, x):
    return 0 <= y < grid_state["height"] and 0 <= x < grid_state["width"]


def find_region(grid_state, target, y, x, visited):
    if not is_valid(grid_state, y, x):
        return set()

    if grid_state["grid"][y][x] != target:
        return set()

    if (y, x) in visited:
        return set()

    visited.add((y, x))
    region = {(y, x)}

    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        region.update(
            find_region(grid_state, target, y + direction[0], x + direction[1], visited)
        )

    return region


def find_all_regions(grid_state):
    visited = set()
    regions = []

    for y, row in enumerate(grid_state["grid"]):
        for x, cell in enumerate(row):
            if (y, x) not in visited:
                region = find_region(grid_state, cell, y, x, set())
                visited.update(region)
                regions.append(region)

    return regions


def calculate_corners(region):
    seen = set()
    corners = 0

    for y, x in region:
        for dy, dx in [
            (-0.5, -0.5),
            (0.5, -0.5),
            (0.5, 0.5),
            (-0.5, 0.5),
        ]:
            new_y = y + dy
            new_x = x + dx

            if (new_y, new_x) in seen:
                continue

            seen.add((new_y, new_x))

            adjacent = sum(
                (new_y + offset_y, new_x + offset_x) in region
                for offset_y, offset_x in [
                    (-0.5, -0.5),
                    (0.5, -0.5),
                    (0.5, 0.5),
                    (-0.5, 0.5),
                ]
            )

            if adjacent == 1 or adjacent == 3:
                corners += 1
            elif adjacent == 2:
                diagonal = [
                    (new_y - 0.5, new_x - 0.5) in region,
                    (new_y + 0.5, new_x + 0.5) in region,
                ]

                if diagonal == [True, True] or diagonal == [False, False]:
                    corners += 2

    return corners


def solve_part_2(grid_state):
    regions = find_all_regions(grid_state)
    result = 0

    for region in regions:
        area = len(region)
        corners = calculate_corners(region)
        result += area * corners

    return result


def main():
    grid_state = generate_grid("Python/d12/input.txt")

    res = solve_part_2(grid_state)
    print("Res: ", res)


if __name__ == "__main__":
    main()
