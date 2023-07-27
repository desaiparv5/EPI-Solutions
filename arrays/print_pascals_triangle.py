def n_rows_pascal_triangle(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    matrix[0][0] = 1
    for i in range(1, n):
        matrix[i][0] = 1
        for j in range(1, i + 1):
            matrix[i][j] = matrix[i - 1][j - 1] + matrix[i-1][j]
    return matrix


def nth_row_pascal_triangle(n):
    row = [1]
    for i in range(1, n+1):
        # compute the i-th element of the current row
        element = row[-1] * (n-i+1) // i
        row.append(element)
    return row


def main():
    n = 10
    triangle = n_rows_pascal_triangle(n)
    print(*triangle, sep="\n", end="\n\n")

    print(nth_row_pascal_triangle(9))


if __name__ == "__main__":
    main()
