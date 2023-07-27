def rotate_matrix_clockwise(matrix):
    reflect_matrix_diagonal_top_left_bottom_right(matrix)
    reflect_matrix_vertical(matrix)


def rotate_matrix_anticlockwise(matrix):
    reflect_matrix_vertical(matrix)
    reflect_matrix_diagonal_top_left_bottom_right(matrix)


def reflect_matrix_vertical(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])//2):
            target_col = len(matrix[0]) - col - 1
            matrix[row][col], matrix[row][target_col] = matrix[row][target_col], matrix[row][col]


def reflect_matrix_horizontal(matrix):
    for row in range(len(matrix)//2):
        for col in range(len(matrix[0])):
            target_row = len(matrix[0]) - row - 1
            matrix[row][col], matrix[target_row][col] = matrix[target_row][col], matrix[row][col]


def reflect_matrix_diagonal_top_left_bottom_right(matrix):
    for col in range(len(matrix[0])):
        for row in range(col, len(matrix)):
            if col == row: continue
            matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]


def reflect_matrix_diagonal_top_right_bottom_left(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0]) - row - 1, -1, -1):
            if col == len(matrix[0]) - row - 1: continue
            target_row = len(matrix[0]) - col - 1
            target_col = len(matrix) - row - 1
            matrix[row][col], matrix[target_row][target_col] = matrix[target_row][target_col], matrix[row][col]


def main():
    from copy import deepcopy

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    mat = deepcopy(matrix)
    rotate_matrix_clockwise(mat)
    print("Clockwise rotation")
    print(*mat, sep="\n", end="\n\n")

    mat = deepcopy(matrix)
    rotate_matrix_anticlockwise(mat)
    print("Anti clockwise rotation")
    print(*mat, sep="\n", end="\n\n")

    mat = deepcopy(matrix)
    reflect_matrix_vertical(mat)
    print("Reflect on vertical axis")
    print(*mat, sep="\n", end="\n\n")

    mat = deepcopy(matrix)
    reflect_matrix_horizontal(mat)
    print("Reflect on horizontal axis")
    print(*mat, sep="\n", end="\n\n")

    mat = deepcopy(matrix)
    reflect_matrix_diagonal_top_left_bottom_right(mat)
    print("Reflect on top left to bottom right diagonal")
    print(*mat, sep="\n", end="\n\n")

    mat = deepcopy(matrix)
    reflect_matrix_diagonal_top_right_bottom_left(mat)
    print("Reflect on top right to bottom left diagonal")
    print(*mat, sep="\n", end="\n\n")


if __name__ == "__main__":
    main()
