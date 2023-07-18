"""Reverse digits of an integer"""


def reverse_digits(num):
    sign = num < 0
    ans = 0
    while num:
        ans = (ans * 10) + (num % 10)
        num //= 10
    return -ans if sign else ans

def main():
    print(reverse_digits(1234))


if __name__ == "__main__":
    main()
