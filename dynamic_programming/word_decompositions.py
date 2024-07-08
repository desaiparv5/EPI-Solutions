from typing import List


def word_decompositions(s: str, words: List[str]):
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True
    for i in range(len(s) - 1, -1, -1):
        for w in words:
            if (i + len(w)) <= len(s) and s[i:i+len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break
    return dp[0]


def word_decompositions_variant_1(s: str):
    # Variant: Every string s has at least one palindromic decomposition, which is the trivial one consisting
    # of the individual characters. For example, if s is "0204451881" then "0", "2", "0", "4", "4", "5",
    # "1", "8", "8", "1" is such a trivial decomposition. The minimum decomposition of s is "020" , "44" , "5" ,
    # "1881.". How would you compute a palindromic decomposition of a string s that uses a minimum
    # number of substrings?
    pass


def main():
    print(word_decompositions("applepenapple", ["apple","pen"]))


if __name__ == "__main__":
    main()