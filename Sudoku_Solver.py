from pprint import pprint
    # sudoku solver using backtracking technique
    # for empty spaces we will use zeroes
    # rule_1: no number should repeat in the 3*3 matrix of 9 matrices
    # rule 2: no number should repeat in the row or column
    # by following above rules we will give the code

def next_empty(puzzle):

    # here we are finding the empty place that present in the puzzle
    # the empty place will be found if it is equal to 0
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c
    return None, None
    # here we are returning None because if there are no 0s present in the puzzle it returns it's solved

def valid(puzzle, guess, row, col):

    # here we will follow sudoku rules
    # we finds which is right fot the col and row
    # returns True if it is valid, otherwise False
    # every list in the puzzle represents row in the puzzle

    row_vals = puzzle[row]

    # here we will return False if this is already in the row
    if guess in row_vals:
        return False
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])
    if guess in col_vals:
        return False

    # from here we will focus on the 3*3 matrix
    # row_st and col_st represents row start and column start respectively

    row_st = (row // 3)*3
    col_st = (col // 3)*3

    for r in range(row_st, row_st + 3):
        for c in range(col_st, col_st + 3):
            if puzzle[r][c] == guess:
                return False

    # if none of the conditions returns False, we need to return True

    return True



def solver(puzzle):

    # our puzzle is a lists of list, where inner list is a row in the sudoku solver
    t = 0
    row, col = next_empty(puzzle)

    if row is None:
        return True

    for guess in range(1,10):
        if valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            # here we are mutuating the puzzle
            if solver(puzzle):
                return True

    # if not valid OR doesn't solve the problem then we need to backtrack the loop

        puzzle[row][col] = 0

        # if nothing returns True then this is unsolvable puzzle, return False

    return False

if __name__ == '__main__':
    puzzle = [
        [0, 0, 5, 3, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 7, 0, 0, 1, 0, 5, 0, 0],
        [4, 0, 0, 0, 0, 5, 3, 0, 0],
        [0, 1, 0, 0, 7, 0, 0, 0, 6],
        [0, 0, 3, 2, 0, 0, 0, 8, 0],
        [0, 6, 0, 5, 0, 0, 0, 0, 9],
        [0, 0, 4, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 9, 7, 0, 0]
    ]
    print(solver(puzzle))
    pprint(puzzle)