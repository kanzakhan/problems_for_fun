'''
You will write a function that checks sudoku squares for correctness.
Sudoku is a logic puzzle where a game is defined by a partially filled 9 x 9 square of digits where each square contains one of the digits 1, 2, 3, 4, 5, 6, 7, 8, 9. For this question we will generalize and simplify the game.
Define a procedure, check_sudoku, that takes as input a square list of lists representing an n x n sudoku puzzle solution and returns the boolean True if the input is a valid sudoku square and returns the boolean False otherwise.

A valid sudoku square satisfies these two properties:
1. Each column of the square contains each of the whole numbers from 1 to n exactly once.
2. Each row of the square contains each of the whole numbers from 1 to n exactly once.
You may assume that the input is square and contains at least one row and column.
'''

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
# Define a function check_sudoku() here:
def check_sudoku(square_list):
    
    rows_valid = check_rows(square_list)
    if not rows_valid:
        return False
    
    cols_valid = check_columns(square_list)
    if not cols_valid:
        return False

    return True
    
def check_rows(square_list):
    # check all rows:
    for row in square_list:
        if is_valid(row):
            continue
        else:
            return False
    return True
    

def check_columns(square_list):
    # now call check_rows on transposed list
    return check_rows(transpose_list(square_list))

# returns transposed list from 2-D input with zip
def transpose_list(square_list):
    # transpose the original nxn list so that columns are now rows
    square_list_transposed = [*zip(*square_list)]

    # convert tuples from *zip to lists with map, then convert map object to list
    square_list_transposed = list(map(list, square_list_transposed))

    return square_list_transposed

# Each row contains each of the whole numbers from 1 to n exactly once
def is_valid(row):
    if no_duplicates(row) and valid_nums(row):
        return True
    else:
        return False

# returns True if all values in list unique
def no_duplicates(input_list):
    return len(set(input_list)) == len(input_list)

# returns True if all values are int and no greater than 'n'
def valid_nums(num_list):
    max_digit = len(num_list)
    for num in num_list:
        if isinstance(num, int) and num > 0 and num <= max_digit:
            continue
        else:
            return False
    return True

    
print(check_sudoku(incorrect) == False)
print(check_sudoku(incorrect2) == False)
print(check_sudoku(incorrect3) == False)
print(check_sudoku(incorrect4) == False)
print(check_sudoku(incorrect5) == False)
print(check_sudoku(correct) == True)
