def traverse_2d_array(rows, cols):
    dp = [[-1]*cols for _ in range(rows)]
    def helper(row, col):
        if dp[row][col] == -1:
            if col == 0 or row == 0:
                dp[row][col] = 1
            else:
                dp[row][col] = helper(row-1, col) + helper(row, col-1)
        return dp[row][col]
    helper(rows - 1, cols - 1)
    return dp[-1][-1]


def traverse_2d_array_1(rows, cols):
    #  Solve the same problem using O(min(n,m)) space.
    if rows > cols:
        rows, cols = cols, rows
    dp = [1]*rows
    aux = [1]*rows
    for _ in range(1, cols):
        for row in range(1, rows):
            dp[row] = aux[row] + dp[row - 1]
        aux = dp
    return dp[-1]


def traverse_2d_array_2(grid):
    # Solve the same problem in the presence of obstacles, specified by a Boolean 2D array, where
    # the presence of a true value represents an obstacle.
    rows = len(grid)
    cols = len(grid[0])
    if grid[rows-1][cols-1] or grid[0][0]:
        return 0
    grid[0][0] = 1
    for i in range(1, rows):
        if grid[i][0]:
            grid[i][0] = 0
        else:
            grid[i][0] = grid[i-1][0]
    for i in range(1, cols):
        if grid[0][i]:
            grid[0][i] = 0
        else:
            grid[0][i] = grid[0][i-1]
    for row in range(1, rows):
        for col in range(1, cols):
            if grid[row][col]:
                grid[row][col] = 0
            else:
                grid[row][col] = grid[row-1][col] + grid[row][col-1]
    return grid[-1][-1]


def traverse_2d_array_3(grid):
    # A fisherman is in a rectangular sea. The value of the fish at point (i, j) in the sea is specified
    # by an n x m 2D array A. Write a program that computes the maximum value of fish a fisherman
    # can catch on a path from the upper leftmost point to the lower rightmost point.
    rows = len(grid)
    cols = len(grid[0])
    for i in range(1, rows):
        grid[i][0] += grid[i-1][0]
    for i in range(1, cols):
        grid[0][i] += grid[0][i-1]
    for row in range(1, rows):
        for col in range(1, cols):
            grid[row][col] += max(grid[row-1][col], grid[row][col-1])
    return grid[-1][-1]


def traverse_2d_array_4(grid):
    # Solve the same problem when the fisherman can begin and end at any point. He must still
    # move down or right
    pass


def traverse_2d_array_5(k):
    # A decimal number is a sequence of digits, i.e., a sequence over {0,1,2, . . . ,9}. The sequence
    # has to be of length 1 or more, and the first element in the sequence cannot be 0. Call a decimal
    # number D monotone if D[i] <= D[i+1], 0 < i < |D|. Write a program which takes as input a positive
    # integer k and computes the number of decimal numbers of length k that are monotone
    digits = 9
    dp = [[0]*digits for _ in range(k)]
    dp[0][0] = 1
    for col in range(1, digits):
        dp[0][col] = 1 + dp[0][col-1]
    for row in range(1, k):
        dp[row][0] = dp[row-1][0]
    
    for col in range(1, digits):
        for row in range(1, k):
            dp[row][col] = dp[row-1][col] + dp[row][col-1]
    return dp[-1][-1]


def traverse_2d_array_6(k):
    # Call a decimal number D, as defined above, strictly monotone if D[i] < D[i+1], 0 < i < |D|.
    # Write a program which takes as input a positive integer k and computes the number of decirnal
    # numbers of length k that are strictly monotone.
    digits = 9
    dp = [[0]*digits for _ in range(k)]
    dp[0][0] = 1
    for col in range(1, digits):
        dp[0][col] = 1 + dp[0][col-1]
    
    for col in range(1, digits):
        for row in range(1, k):
            dp[row][col] = dp[row-1][col-1] + dp[row][col-1]
    return dp[-1][-1]


def main():
    print(traverse_2d_array(12,23))
    print(traverse_2d_array_1(12,23))
    print(traverse_2d_array_2([[0,0,0],[0,1,0],[0,0,0]]))
    print(traverse_2d_array_3([[1,3,0],[0,1,5],[3,2,4]]))
    print(traverse_2d_array_5(2))
    print(traverse_2d_array_6(3))


if __name__ == "__main__":
    main()
