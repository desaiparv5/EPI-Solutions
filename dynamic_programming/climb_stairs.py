def climb_stairs(num_steps, max_step):
    dp = [0]*(num_steps + 1)
    def helper(n):
        if n <= 1:
            return 1
        if dp[n] == 0:
            dp[n] = sum(helper(n-i) for i in range(1, min(max_step, n) + 1))
        return dp[n]
    return helper(num_steps)


def main():
    print(climb_stairs(4, 2))


if __name__ == "__main__":
    main()
