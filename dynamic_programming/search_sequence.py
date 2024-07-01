def search_sequence(seq, grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    previous_attempts = set()
    def helper(row, col, ind):
        if ind == len(seq):
            return True
        if 0 <= row < rows and 0 <= col < cols and seq[ind] == grid[row][col] and (row, col, ind) not in previous_attempts:
            previous_attempts.add((row, col, ind))
            return any(helper(row+x,col+y,ind+1) for x, y in directions)
        return False
    return any(helper(row, col, 0) for row in range(rows) for col in range(cols))


def search_sequence_variant_1(seq, grid):
    # TODO: Solve the same problem when you cannot visit an entry in grid more than once.
    pass


def search_sequence_variant_2(seq, grid):
    # TODO: Enumerate all solutions when you cannot visit an entry in grid more than once.
    pass


def main():
    print(search_sequence(grid=[[1,2,3],[4,5,6],[7,8,9]], seq = [1,4,7,8,6]))


if __name__ == "__main__":
    main()
