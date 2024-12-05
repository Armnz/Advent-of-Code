# Function to count occurrences of "XMAS" in all directions
def count_xmas_occurrences(input_string):
    # Parse the grid
    lines = input_string.splitlines()
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = max(len(line) for line in grid)  # Allow for irregular grids

    # Normalize the grid to ensure all rows have the same length
    for row in grid:
        row.extend([" "] * (cols - len(row)))  # Pad with spaces for shorter rows

    # Directions to search for the word "XMAS"
    directions = [
        (0, 1),  # Right
        (1, 0),  # Down
        (0, -1), # Left
        (-1, 0), # Up
        (1, 1),  # Down-Right
        (-1, -1),# Up-Left
        (1, -1), # Down-Left
        (-1, 1), # Up-Right
    ]

    # Function to search for the word "XMAS" starting at (r, c) in a given direction
    def search_word(r, c, dr, dc):
        word = "XMAS"
        for i in range(len(word)):
            nr, nc = r + i * dr, c + i * dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != word[i]:
                return False
        return True

    # Count occurrences of "XMAS"
    count = 0
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if search_word(r, c, dr, dc):
                    count += 1

    return count

with open('input.txt', 'r') as file:
    input_string = file.read()

result = count_xmas_occurrences(input_string)
print(f"The total occurrences of 'XMAS' are: {result}")

#The total occurrences of 'XMAS' are: 2534


#####--- Part Two ---#####


def count_xmas_x_shapes(input_string):
    # Parse the grid
    lines = input_string.splitlines()
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = max(len(line) for line in grid)  # Allow for irregular grids

    # Normalize the grid to ensure all rows have the same length
    for row in grid:
        row.extend([" "] * (cols - len(row)))  # Pad with spaces for shorter rows

    # Function to check for an X-MAS shape centered at (r, c)
    def is_xmas_shape(r, c):
        # Ensure the pattern fits in the grid
        if (
            r - 1 >= 0 and r + 1 < rows and c - 1 >= 0 and c + 1 < cols
        ):
            # Top-left and bottom-right diagonal: either "MAS" or "SAM"
            diag1 = (
                grid[r - 1][c - 1],
                grid[r][c],
                grid[r + 1][c + 1]
            )
            # Top-right and bottom-left diagonal: either "MAS" or "SAM"
            diag2 = (
                grid[r - 1][c + 1],
                grid[r][c],
                grid[r + 1][c - 1]
            )

            # Valid X-MAS configurations
            valid_mas = [("M", "A", "S"), ("S", "A", "M")]

            # Check if both diagonals form valid X-MAS
            return diag1 in valid_mas and diag2 in valid_mas
        return False

    # Count occurrences of X-MAS shapes
    count = 0
    for r in range(rows):
        for c in range(cols):
            if is_xmas_shape(r, c):
                count += 1

    return count

with open('input.txt', 'r') as file:
    input_string = file.read()

result = count_xmas_x_shapes(input_string)
print(f"The total occurrences of X-MAS shapes are: {result}")

#The total occurrences of X-MAS shapes are: 1866