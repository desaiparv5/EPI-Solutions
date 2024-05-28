def solve_sudoku(board):

    def is_valid_entry(row, col):
        # check column
        for i in range(len(board)):
            if board[i][col] == board[row][col] and i != row:
                return False
        # check row
        for j in range(len(board[0])):
            if board[row][j] == board[row][col] and j != col:
                return False
        # check subgrid
        for i in range(row//3*3, (row+3)//3*3):
            for j in range(col//3*3, (col+3)//3*3):
                if board[i][j] == board[row][col] and i != row and j != col:
                    return False
        return True

    def helper(row, col):
        if col == len(board):
            col = 0
            row += 1
            if row == len(board):
                return True
        if board[row][col] != ".":
            return helper(row, col + 1)
        for dig in range(1, 10):
            board[row][col] = str(dig)
            if is_valid_entry(row, col):
                if helper(row, col + 1):
                    return True
            board[row][col] = "."
    helper(0, 0)

def main():
    partial_sudoku = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    solve_sudoku(partial_sudoku)
    print(partial_sudoku)

if __name__ == "__main__":
    main()


