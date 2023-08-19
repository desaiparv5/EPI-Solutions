def search_2d_sorted_matrix(matrix, element):
    rows = len(matrix)
    columns = len(matrix[0])
    def _helper(row, column):
        if column < 0 or row >= rows:
            return -1, -1
        if element == matrix[row][column]:
            return (row, column)
        elif element > matrix[row][column]:
            return _helper(row + 1, column)
        return _helper(row, column - 1)
    return _helper(0, columns - 1)


def main():
    matrix = [[1,5,6,8],[3,7,9,10],[4,11,16,20]]
    element = 16
    print(search_2d_sorted_matrix(matrix, element))


if __name__ == "__main__":
    main()
