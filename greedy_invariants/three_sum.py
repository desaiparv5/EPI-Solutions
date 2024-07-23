from greedy_invariants.two_sum import has_two_sum


def has_three_sum(arr, target):
    arr.sort()
    return any(has_two_sum(arr, target - a) for a in arr)


def has_three_sum_variant_1():
    # TODO: Solve the same problem when the three elements must be distinct. For example, if A =
    # (5,2,3,4,3) and f = 9, then A[2] + A[2] + A[2] is not acceptable, A[2] + A[2] + A[4]is not acceptable,
    # but A[1] + A[2] + A[3] and A[1] + A[3] + A[4] are acceptable.
    pass


def has_three_sum_variant_2():
    # TODO: Solve the same problem when k, the number of elements to sum, is an additional input.
    pass


def has_three_sum_variant_3():
    # TODO: Write a program that takes as input an array of integers A and an integer T, and returns
    # a 3-tuple (A[p],A[q],A[r]) where p, q, r are all distinct, minimizing |T - (A[p] + A[q] + A[r])|, and
    # A[p] <= A[r] <= A[s].
    pass


def has_three_sum_variant_4():
    # TODO: Write a program that takes as input an array of integers A and an integer T, and returns
    # the number of 3-tuples (p, q, r) such that A[p] + A[q] + A[r] <= T and A[p] <= A[q] <= A[r].
    pass


def main():
    print(has_three_sum([2,6,1,9,0,5,6,1], 6))


if __name__ == "__main__":
    main()
