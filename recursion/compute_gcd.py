def compute_gcd(x, y):
    if y == 0:
        return x
    else:
        return compute_gcd(x, x % y)


def main():
    x = 10
    y = 20
    print(compute_gcd(x, y))


if __name__ == "__main__":
    main()
