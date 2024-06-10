def levensthien_distance(str1, str2):
    dp = [[-1 for _ in range(len(str1))] for _ in range(len(str2))]
    def helper(row, col):
        if row < 0:
            return col + 1
        elif col < 0:
            return row + 1
        if dp[row][col] == -1:
            if str1[col] == str2[row]:
                dp[row][col] = helper(row-1, col-1)
            else:
                substitute = helper(row-1, col-1)
                deletion = helper(row, col-1)
                insertion = helper(row-1, col)
                dp[row][col] = 1 + min(substitute, deletion, insertion)
        return dp[row][col]
    return helper(len(str2) - 1, len(str1) - 1)


def levensthien_distance_variant_1():
    # TODO
    # Compute the Levenshtein distance using O(min(a, b)) space and O(ab) time.
    pass


def levensthien_distance_variant_2():
    # TODO
    # Given A and B as above, compute a longest sequence of characters that is a subsequence
    # of A and of B. For example, the longest subsequence which is present in both strings
    # is (r,h,s).
    pass


def levensthien_distance_variant_3():
    # TODO
    # Given a string A, compute the minimum number of characters you need to delete from A
    # to make the resulting string a palindrome.
    pass


def levensthien_distance_variant_4():
    # TODO
    # Given a string A and a regular expression r, what is the string in the language of the regular
    # expression r that is closest to A? The distance between strings is the Levenshtein distance specified
    # above.
    pass


def levensthien_distance_variant_5():
    # TODO
    # Define a string f to be an interleaving of strings s1 and s2 if there is a way to interleave
    # the characters of s1 and s2, keeping the left-to-right order of each, to obtain f.
    pass


def main():
    print(levensthien_distance("Carthorse", "Orchestra"))
    print(levensthien_distance("intent", "in"))
    print(levensthien_distance("horse", "ros"))


if __name__ == "__main__":
    main()
