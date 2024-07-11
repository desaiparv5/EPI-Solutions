def pick_coins(coins):
    n = len(coins)
    dp = [[0]*n for _ in range(n)]

    for i in range(n):
        dp[i][i] = coins[i]

    for gap in range(n):
        for col in range(gap, n):
            row = col - gap
            if gap == 0:
                option_a = option_b = coins[row]
            elif gap == 1:
                option_a = dp[row+1][col]
                option_b = dp[row][col-1]
            else:
                option_a = coins[row] + min(dp[row+2][col], dp[row+1][col-1])
                option_b = coins[col] + min(dp[row][col-2], dp[row+1][col-1])
            dp[row][col] = max(option_a, option_b)
    return dp[0][-1]


def main():
    print(pick_coins([20,30,2,10]))


if __name__ == "__main__":
    main()
