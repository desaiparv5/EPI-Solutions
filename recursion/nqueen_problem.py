def n_queens(n):
    result, col_placement = [], [0] * n
    def solve_n_queens(row):
        if row == n:
            result.append(list(col_placement))
            return
        for col in range(n):
            q = [abs(c - col) not in (0, row - i) for i, c in enumerate(col_placement[:row])]
            if all(q):
                col_placement[row] = col
                solve_n_queens(row + 1)
    solve_n_queens(0)
    return result


def num_of_placements(*args, **kwargs):
    """Compute the number of nonattacking placements of n queens on an n x n chessboard."""
    pass


def attack_uncovered_squared(*args, **kwargs):
    """Compute the smallest number of queens that can be placed to attack each uncoveredsquare."""
    pass


def knights_bishops_kings_rooks(*args, **kwargs):
    """Variant Compute a placement of 32 knights, or 14 bishops, 16 kings or 8 rooks on an 8 x 8
    chessboard in which no two pieces attack each other"""
    pass


def main():
    n = 10
    print(n_queens(n))


if __name__ == "__main__":
    main()
