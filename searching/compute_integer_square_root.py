def compute_integer_square_root(number):
    def _helper(low, high):
        if low > high:
            return low - 1
        mid = low + (high - low) // 2
        square = mid * mid
        if square == number:
            return mid
        elif square > number:
            return _helper(low, mid - 1)
        return _helper(mid + 1, high)
    return _helper(0, number)


def main():
    number = 225
    print(compute_integer_square_root(number))


if __name__ == "__main__":
    main()
