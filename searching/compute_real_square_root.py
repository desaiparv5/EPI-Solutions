from compute_integer_square_root import compute_integer_square_root


def compute_real_square_root(number, precision):
    answer = compute_integer_square_root(number) if number > 1 else 0
    increment = 0.1
    for _ in range(precision):
        while answer * answer < number:
            answer += increment
        answer -= increment
        increment /= 10
    return round(answer, precision)


def compute_integer_division(x, y):
    def _helper(low, high):
        if low > high:
            return low - 1
        mid = low + (high - low) // 2
        product = mid * y
        if product == x:
            return mid
        elif product < x:
            return _helper(mid + 1, high)
        return _helper(low, mid - 1)
    return 0 if x < y else _helper(1, x)


def compute_division(x, y, precision):
    answer = compute_integer_division(x, y)
    increment = 0.1

    for _ in range(precision):
        while answer * y < x:
            answer += increment
        answer -= increment
        increment /= 10
    
    return round(answer, precision)


def main():
    number = 225
    print(compute_real_square_root(number, 4))
    print(compute_division(124, 3, 4))


if __name__ == "__main__":
    main()
