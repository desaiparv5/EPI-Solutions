from collections import Counter


def palindromic_permutation(string):
    return sum([v % 2 for v in Counter(string).values()]) <= 1


def main():
    string = "aaab"
    print(palindromic_permutation(string))


if __name__ == "__main__":
    main()
