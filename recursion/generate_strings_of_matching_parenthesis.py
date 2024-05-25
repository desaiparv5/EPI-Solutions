def generate_parenthesis(n):
    res = []
    def helper(left, right, curr_str):
        if not (left or right):
            res.append(curr_str)
            return
        if left:
            helper(left - 1, right, curr_str + "(")
        if right > left:
            helper(left, right - 1, curr_str + ")")
    helper(n, n, "")
    return res

def main():
    k = 3
    print(generate_parenthesis(k))


if __name__ == "__main__":
    main()
