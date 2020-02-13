import sys
from pprint import pprint

# Sample default board data to use as input (csv format required)
SAMPLE = "420070805,070105602,061090004,904002051,050301069,610009000,802000000,090824500,040906020"

sudoku = []


def make_board(raw):
    # Creates and checks board from input

    # Check correct number of characters in raw input
    if len(raw) != 9 * 9 + 8:
        print("Incorrect input format")
        sys.exit(1)

    # Convert into list of rows
    rows = raw.split(',')
    if len(rows) != 9:
        print("Incorrect number of rows")
        sys.exit(1)

    # Check correct number of rows
    counter = 1
    for row in rows:
        if len(row) != 9:
            print(f"Row {counter} is not the correct length")
            sys.exit(1)
        # Convert each row into a list of numbers
        try:
            sudoku.append([int(c) for c in row])
            counter += 1
        except ValueError:
            print("Non-numerical input entered")
            sys.exit(1)
    # If all successful -> display starting board
    print("\nStarting board:")
    pprint(sudoku)


def check(n, row, col):
    # Check whether candidate number can fit in current board

    # Check within row
    for i in range(9):
        if n == sudoku[row][i]:
            return False
    # Check within column
    for j in range(9):
        if n == sudoku[j][col]:
            return False
    # Check within 3x3 square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if sudoku[i][j] == n:
                return False
    return True


def find_zero():
    # Finds next unassigned number (if any)

    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return [i, j, True]
    else:
        return [-1, -1, False]


def solve():

    # Get co-ordinates of next unassigned number
    row, col, found = find_zero()
    # If no unassigned numbers found -> sudoku solved
    if not found:
        return True
    # Cycle through candidate numbers
    for n in range(1, 10):
        if check(n, row, col):
            # Replace unassigned number suitable candidate number
            sudoku[row][col] = n
            # Check the rest of the board using this number
            if solve():
                return True
            # If candidate does not work -> check next potential candidate number
            sudoku[row][col] = 0
    # If all candidates exhausted -> back-track
    return False


# Get input
raw = input("Enter the board: ")
raw = SAMPLE if raw == "" else raw

# Make and solve board
make_board(raw)
solved = solve()

# Display results
if solved:
    print("\nFound a solution:")
    pprint(sudoku)
    print()
else:
    print("\nCould not find a solution")
