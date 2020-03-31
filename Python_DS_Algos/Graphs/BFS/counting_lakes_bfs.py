def numberOfLakes(rows, column, grid):
    # Edge case 1: empty grid
    if not grid:
        return 0

    visited_idx = set()
    num_lakes = 0

    for i in range(rows):
        for j in range(column):
            if(grid[i][j]) == 1 and (i,j) not in visited_idx:
                breadth_first_search(rows, column, grid, i, j, visited_idx)
                num_lakes += 1
    
    return num_lakes
        
def breadth_first_search(rows, cols, grid, i, j, visited_idx):
    
    # must be tuple (immutable) since this will be key for visited_idx set
    positions_to_check = [(i,j)]

    while positions_to_check:

        check_again = []
        for position in positions_to_check:

            # check if already vistied this position
            if position in visited_idx:
                continue
            
            # mark position as visited by adding to set
            visited_idx.add(position)
            i = position[0]
            j = position[1]

            # make sure all positions within bounds of grid
            # check left
            if j - 1 >= 0 and grid[i][j - 1] == 1:
                check_again.append((i, j - 1))
            # check right
            if j + 1 < cols and grid[i][j + 1] == 1:
                check_again.append((i, j + 1))
            # check above
            if i - 1 >= 0 and grid[i - 1][j] == 1:
                check_again.append((i - 1, j))
            # check below
            if i + 1 < rows and grid[i + 1][j] == 1:
                check_again.append((i + 1, j))

        # now check the positions already visited that were 1s to see the neighbors for them
        positions_to_check = check_again
            


def main(): 
    rows = 5
    column = 4
    grid = [
        [1,1,0,0],
        [0,0,1,0],
        [0,0,0,0],
        [1,0,1,1],
        [1,1,1,1]
    ]
    print(numberOfLakes(rows, column, grid) == 3)

main()
