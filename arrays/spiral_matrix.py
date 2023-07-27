from copy import deepcopy


def spiral_matrix(matrix):
    def print_spiral(matrix, row):
        right_column = len(matrix[0]) - row - 1
        bottom_row = len(matrix) - row - 1
        left_column = row
        top_row = row

        if top_row == right_column:
            yield(matrix[top_row][right_column])
            return

        # top row
        for i in range(left_column, right_column):
            yield(matrix[top_row][i])
        
        # right column
        for i in range(top_row, bottom_row):
            yield(matrix[i][right_column])

        # bottom row
        for i in range(right_column, left_column, -1):
            yield(matrix[bottom_row][i])

        # left column
        for i in range(bottom_row, top_row, -1):
            yield(matrix[i][left_column])

    for i in range(len(matrix) // 2 + 1):
        yield from print_spiral(matrix, i)


def spiral_matrix_pro(matrix):
    direction = 0
    shift = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x = 0
    y = 0

    for _ in range(len(matrix[0])*len(matrix)):
        yield(matrix[x][y])
        matrix[x][y] = None

        next_x = x + shift[direction][0]
        next_y = y + shift[direction][1]
        if (next_x >= len(matrix) or next_y >= len(matrix[0]) or next_x < 0 or next_y < 0) or not matrix[next_x][next_y]:
            direction = (direction + 1) % 4
            next_x = x + shift[direction][0]
            next_y = y + shift[direction][1]

        x = next_x
        y = next_y


def spiral_matrix_zip(matrix):
    return matrix and list(matrix.pop(0)) + spiral_matrix_zip([*zip(*matrix)][::-1])


def generate_sprial_matrix(array):
    dimension = int(len(array)**0.5)
    matrix = [[None for _ in range(dimension)] for _ in range(dimension)]

    direction = 0
    shift = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x = 0
    y = 0

    for val in array:
        matrix[x][y] = val

        next_x = x + shift[direction][0]
        next_y = y + shift[direction][1]
        if (next_x >= len(matrix) or next_y >= len(matrix[0]) or next_x < 0 or next_y < 0) or matrix[next_x][next_y] is not None:
            direction = (direction + 1) % 4
            next_x = x + shift[direction][0]
            next_y = y + shift[direction][1]

        x = next_x
        y = next_y
    
    return matrix


def generate_sequential_spiral_matrix(dimension):
    return generate_sprial_matrix([_ for _ in range(dimension * dimension)])


def points_in_spiral_order(n):
    x = 0
    y = 0
    counter = 0
    turn_after_steps = 1

    shift = [[1,0],[0,-1],[-1,0],[0,1]]
    direction = 0
    while counter < n:
        current_step = 0
        while counter < n and current_step < turn_after_steps:
            yield x, y
            x += shift[direction][0]
            y += shift[direction][1]
            current_step += 1
            counter += 1

        direction = (direction + 1) % 4
        turn_after_steps += 1 if direction % 2 == 0 else 0


def kth_element_in_spiral_order(matrix, k):

    if not matrix:
        return 0
    rows = len(matrix)
    columns = len(matrix[0])

    if k < columns:
        return matrix[0][k]
    if k < (rows + columns - 1):
        return matrix[k - columns + 1][-1]
    if k < (2 * columns + rows - 2):
        return matrix[-1][2 * columns + rows - 3 - k]
    if k < (2 * columns + 2 * rows - 4):
        return matrix[k - (2 * columns + 2 * rows - 4) + 2][0]
    else:
        return kth_element_in_spiral_order([list(val)[1:-1] for val in matrix[1:-1]], k - (2 * rows + 2 * columns - 4))


def last_point_in_spriral_order(matrix):
    num_elements = len(matrix) * len(matrix[0])
    return kth_element_in_spiral_order(matrix, num_elements - 1)


def main():
    matrix = [
        [1, 2, 3, 4],
        [10, 11, 12, 5],
        [9, 8, 7, 6]
    ]

    for i in spiral_matrix(deepcopy(matrix)):
        print(i, end=" ")
    print()

    for i in spiral_matrix_pro(deepcopy(matrix)):
        print(i, end=" ")
    print()

    print(spiral_matrix_zip(deepcopy(matrix)))
    
    print(generate_sprial_matrix([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
    print(generate_sequential_spiral_matrix(4))

    print(last_point_in_spriral_order(deepcopy(matrix)))
    print(kth_element_in_spiral_order(deepcopy(matrix), 7))

    for x, y in points_in_spiral_order(10):
        print(f"({x} {y})", end=", ")


if __name__ == "__main__":
    main()
