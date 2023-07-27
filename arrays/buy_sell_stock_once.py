"""Maximum profit by buying and selling stock once."""

def buy_sell_stock_once(arr):
    if not arr:
        return 0

    min_price = arr[0]
    max_profit = 0

    for ind in range(1, len(arr)):
        min_price = min(arr[ind], min_price)
        max_profit = max(max_profit, arr[ind] - min_price)
    return max_profit


def longest_subarray_with_equal_values(arr):
    if not arr: return 0
    max_freq = 0
    curr_freq = 1

    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            curr_freq += 1
        else:
            max_freq = max(max_freq, curr_freq)
            curr_freq = 1
    return max_freq


def main():
    arr = [1, 3, 2, 2, 4, 4, 4, 4, 6]
    print(buy_sell_stock_once(arr))
    print(longest_subarray_with_equal_values(arr))


if __name__ == "__main__":
    main()
