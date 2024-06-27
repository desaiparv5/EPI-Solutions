def compute_binomial_coefficients(n, k):
    if n < k:
        raise Exception
    dp = [[0]*(n+1) for _ in range(k+1)]
    for col in range(n+1):
        dp[0][col] = 1
    for row in range(k+1):
        dp[row][row] = 1
    for row in range(1, k+1):
        for col in range(row, n+1):
            dp[row][col] = dp[row-1][col-1] + dp[row][col-1]
    return dp[k][n]


def main():
    print(compute_binomial_coefficients(10, 4))
    print(compute_binomial_coefficients(5,2))


if __name__ == "__main__":
    main()
