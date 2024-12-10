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


def calculate_trail_heads(grid):

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "9":
                calculate_path(grid, x, y)


def main():
    grid = generate_grid("d10/small.txt")
    calculate_trail_heads(grid)


if __name__ == "__main__":
    main()
