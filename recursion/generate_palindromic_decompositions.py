def palindromic_decompositions(s):
    res = []
    def helper(curr_index, curr_list):
        if curr_index == len(s):
            res.append(curr_list.copy())
            return
        for i in range(curr_index, len(s)):
            if s[curr_index:i+1] == s[curr_index:i+1][::-1]:
                helper(i+1, curr_list + [s[curr_index:i+1]])
    helper(0, [])
    return res

def palindrome_decompositions_pythonic(text):
    return ([[text[:i]] + right for i in range(1, len(text) + 1)
             if text[:i] == text[:i][::-1]
             for right in palindrome_decompositions_pythonic(text[i:])] or [[]])


def main():
    s = "aaab"
    print(palindromic_decompositions(s))
    print(palindrome_decompositions_pythonic(s))

if __name__ == "__main__":
    main()