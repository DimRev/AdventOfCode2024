DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def parse_file(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def set_dimensions(grid):
    global WIDTH, HEIGHT
    HEIGHT = len(grid)
    WIDTH = len(grid[0]) if grid else 0


def generate_grid(path):
    grid = []
    row = []
    for line in parse_file(path):
        for char in line:
            row.append(char)
        grid.append(row)
        row = []
    set_dimensions(grid)
    return grid


DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def is_valid(y, x):
    return 0 <= y < HEIGHT and 0 <= x < WIDTH


def dfs_from_trailhead(grid, start_y, start_x, start_h=0):

    if not is_valid(start_y, start_x):  # Pointers are out of bounds
        return 0
    if grid[start_y][start_x] != str(start_h):  # The curr cell isn't an increment
        return 0
    if grid[start_y][start_x] == "9":  # Reached target
        return 1

    total_routes = 0

    nh = start_h + 1
    for dy, dx in DIRECTIONS:
        ny, nx = start_y + dy, start_x + dx
        total_routes += dfs_from_trailhead(grid, ny, nx, nh)

    return total_routes


# Main logic
def solve(grid):
    total_paths = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "0":
                total_paths += dfs_from_trailhead(grid, y, x)
    return total_paths


def main():
    # grid = generate_grid("Python/d10/small.txt")
    grid = generate_grid("Python/d10/input.txt")
    total_paths = solve(grid)
    print(total_paths)


if __name__ == "__main__":
    main()
