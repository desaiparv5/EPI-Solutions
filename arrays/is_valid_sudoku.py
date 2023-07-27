columns = 9
rows = 9
region_size = 3


def has_any_duplicates(arr, row_start, row_end, col_start, col_end):
    num_seen = set()
    for i in range(row_start, row_end + 1):
        for j in range(col_start, col_end + 1):
            if arr[i][j] == ".": continue
            elif arr[i][j] in num_seen: return True
            else: num_seen.add(arr[i][j])
    return False


def is_valid_sudoku(arr):
    for i in range(columns):
        if has_any_duplicates(arr, 0, rows, i, i):
            return False
    
    for i in range(rows):
        if has_any_duplicates(arr, i, i, 0, columns):
            return False

    for i in range(0, rows, region_size):
        for j in range(0, columns, region_size):
            if has_any_duplicates(arr, i, i+region_size, j, j+region_size):
                return False

    return True


def main():
    arr = [
        ["1",".",".",".",".",".",".",".",".","."],
        [".","1",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."]
    ]
    print(is_valid_sudoku(arr))


if __name__ == "__main__":
    main()
