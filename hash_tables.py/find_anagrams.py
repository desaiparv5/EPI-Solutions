from collections import defaultdict


def find_anagrams(array):
    sorted_strings = defaultdict(list)
    for arr in array:
        sorted_strings["".join(sorted(arr))].append(arr)
    return [
        group for group in sorted_strings.values() if len(group) > 1
    ]


def main():
    array = ["debitcard", "elyis", "silent", "badcredit", "lives", "fteedom", "listen", "levis", "money"]
    print(find_anagrams(array))


if __name__ == "__main__":
    main()
