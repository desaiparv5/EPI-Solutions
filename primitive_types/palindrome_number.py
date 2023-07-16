"""Check if number is palindrome or not"""


from reverse_digits import reverse_digits


def is_palindrome(num):
    if num < 0:
        return False
    else:
        return num == reverse_digits(num)


def main():
    print(is_palindrome(121))


if __name__ == "__main__":
    main()
