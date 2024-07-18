import bisect


def lis(seq):
    dp = [1]* len(seq)
    for i in range(len(seq)):
        for j in range(0, i):
            if seq[j] < seq[i]:
                dp[i] = max(dp[i], 1 + dp[j])
    return max(dp)


def lis_variant_1(seq):
    dp = [1]* len(seq)
    h = [-1] * len(seq)
    for i in range(len(seq)):
        for j in range(0, i):
            if seq[j] < seq[i]:
                if 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    h[i] = j
    ans = dp[0]
    pos = h[0]
    for ind, val in enumerate(dp):
        if val > ans:
            ans = val
            pos = ind
    sub = []
    while pos >= 0:
        sub.append(seq[pos])
        pos = h[pos]
    return list(reversed(sub))


def lis_variant_2(seq):
    # Alternating subsequence
    inc = dec = 1
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1]:
            inc = dec + 1
        elif seq[i] < seq[i-1]:
            dec = inc + 1
    return max(inc, dec)


def lis_variant_3(seq):
    # TODO: Define a sequence of numbers (a0, a1, . . . , an-1) to be weakly alternating if no three consecutive
    # terms in the sequence are increasing or decreasing. Given an array of numbers A of length n, and
    # a longest subsequence (i0,...,ik-1) such that (A[i0],A[i1],...,A[ik-i]) is weakly alternating.
    pass


def lis_variant_4(seq):
    # TODO: Define a sequence of numbers (a0,a1,...,an-1) to be convex if ai < (ai-1+ai+1)/2, for 1 < i <
    # n - 2. Given an array of numbers A of length n, find a longest subsequence (i0,...,ik-1) such that
    # (A[i0], A[i1], . . ., A[ik-1]) is convex.
    pass


def lis_variant_5(seq):
    # TODO: Define a sequence of numbers (a0,a1,...,an-1)to be bitonic if there exists k such that ai < ai+1,
    # for 0 <= i < k and ai > ai+1, for k <= i < n- 1. Given an array of numbers A of length n, find a longest
    # subsequence (i0,.. .,ik-1) such that (A[i0],A[i1],... ,A[ik-1]) is bitonic.
    pass


def lis_variant_6(seq):
    # TODO: Define a sequence of points in the plane to be ascending if each point is above and to the
    # right of the previous point. How would you find a maximum ascending subset of a set of points in
    # the plane?
    pass


def lis_variant_7(seq):
    sub = []
    for num in seq[1:]:
        if len(sub) == 0 or num > sub[-1]:
            sub.append(num)
        else:
            ind = bisect.bisect_left(sub, num)
            sub[ind] = num
    return len(sub)


def main():
    print(lis([1,3,6,7,9,4,10,5,6]))
    print(lis_variant_1([1,3,6,7,9,4,10,5,6]))
    print(lis_variant_2([1,3,1,3,1,3,1,3,1]))


if __name__ == "__main__":
    main()
