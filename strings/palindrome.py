def is_palindrome(s):
    for ind in range(len(s)):
        if s[ind] != s[len(s) - ind - 1]: return False
    return True


def main():
    s = "qa"
    print(is_palindrome(s))


if __name__ == "__main__":
    main()
