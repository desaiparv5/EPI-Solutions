def collatz_conjecture(n):
    tested_variables = set()
    for i in range(1, n + 1):
        test_i = i
        sequence = set()
        while test_i >= i:
            if test_i == 1:
                tested_variables.add(i)
                break
            if test_i in sequence:
                return False
            sequence.add(test_i)
            if test_i % 2:
                if test_i in tested_variables:
                    break
                test_i = 3 * test_i + 1
            else:
                test_i //= 2
    return True


def main():
    n = 20
    print(collatz_conjecture(n))


if __name__ == "__main__":
    main()
