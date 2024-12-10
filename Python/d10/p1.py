DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def parse_file(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def generate_grid(path):
    grid = []
    row = []
    for line in parse_file(path):
        for char in line:
            row.append(char)
        grid.append(row)
        row = []
    return grid


DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def is_valid(y, x, HEIGHT, WIDTH):
    return 0 <= y < HEIGHT and 0 <= x < WIDTH


def bfs_from_trailhead(grid, start_y, start_x):
    HEIGHT = len(grid)
    WIDTH = len(grid[0])
    start_height = 0
    reachable_nines = set()
    visited = set()
    queue = [(start_y, start_x, start_height)]

    visited.add((start_y, start_x))

    while queue:
        y, x, h = queue.pop(0)

        if h == 9:
            # Found a trail ending at height 9
            reachable_nines.add((y, x))
            # No need to go beyond 9 since trails end at 9
            continue

        # Try all directions for h+1
        next_height = h + 1
        target_char = str(next_height)
        for dy, dx in DIRECTIONS:
            ny, nx = y + dy, x + dx
            if is_valid(ny, nx, HEIGHT, WIDTH) and grid[ny][nx] == target_char:
                if (ny, nx) not in visited:
                    visited.add((ny, nx))
                    queue.append((ny, nx, next_height))

    return len(reachable_nines)


# Main logic
def solve(grid):
    total_paths = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "0":
                # For each trailhead, count reachable nines
                score = bfs_from_trailhead(grid, y, x)
                total_paths += score
    return total_paths


def main():
    # grid = generate_grid("Python/d10/small.txt")
    grid = generate_grid("Python/d10/input.txt")
    total_paths = solve(grid)
    print(total_paths)


if __name__ == "__main__":
    main()
