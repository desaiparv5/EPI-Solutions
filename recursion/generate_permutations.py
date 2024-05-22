def generate_permutations(arr: list):
    results = []
    def helper(ind):
        if ind == len(arr) - 1:
            results.append(arr.copy())
        for i in range(ind, len(arr)):
            arr[i], arr[ind] = arr[ind], arr[i]
            helper(ind + 1)
            arr[i], arr[ind] = arr[ind], arr[i]
    helper(0)
    return results


def generate_permutations_w_duplicates(arr: list):
    from collections import Counter
    results = []
    def helper(comb, freq):
        if len(comb) == len(arr):
            results.append(comb.copy())
        for num, val in freq.items():
            if val > 0:
                freq[num] -= 1
                comb.append(num)
                helper(comb, freq)
                comb.pop()
                freq[num] += 1
    helper([], Counter(arr))
    return results

def main():
    arr = [1, 1, 2]
    print(generate_permutations(arr))
    print(generate_permutations_w_duplicates(arr))


if __name__ == "__main__":
    main()
