def generate_permutations(arr: list):
    results = []
    def helper(ind):
        if ind == len(arr):
            results.append(arr.copy())
        for i in range(ind, len(arr)):
            arr[i], arr[ind] = arr[ind], arr[i]
            helper(i + 1)
            arr[i], arr[ind] = arr[ind], arr[i] 
    helper(0)
    return results


def main():
    arr = [1, 2, 3]
    print(generate_permutations(arr))


if __name__ == "__main__":
    main()
