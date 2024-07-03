from calendar import c
from typing import List
from collections import namedtuple


Item = namedtuple("Item", ["weight", "value"])


def knapsack_problem(weight: int, items: List[Item]):
    dp = [[-1]*(weight+1) for _ in range(len(items) + 1)]
    for i in range(len(items) + 1):
        dp[i][0] = 0
    for i in range(weight + 1):
        dp[0][i] = 0
    def helper(row, col):
        if row <= 0 or col <= 0:
            return 0
        if dp[row][col] == -1:
            without_curr_item = helper(row-1, col)
            if col < items[row-1].weight:
                with_curr_item = without_curr_item
            else:
                with_curr_item = helper(row - 1, col - items[row-1].weight) + items[row-1].value
            dp[row][col] = max(without_curr_item, with_curr_item)
        return dp[row][col]
    return helper(len(items), weight)


def knapsack_problem_iterative(weight: int, items: List[Item]):
    dp = [[-1]*(weight+1) for _ in range(len(items) + 1)]
    for i in range(len(items) + 1):
        dp[i][0] = 0
    for i in range(weight + 1):
        dp[0][i] = 0
    for row in range(1, len(items)+1):
        for col in range(1, weight + 1):
            without_curr_item = dp[row-1][col]
            if col < items[row-1].weight:
                with_curr_item = without_curr_item
            else:
                with_curr_item = dp[row - 1][col - items[row-1].weight] + items[row-1].value
            dp[row][col] = max(without_curr_item, with_curr_item)
    return dp[-1][-1]


def knapsack_problem_variant_1(weight: int, items: List[Item]):
    # Solve the same problem using O(w) space.
    prev = [0]*(weight+1)
    curr = [0]*(weight+1)
    for row in range(1, len(items)+1):
        for col in range(1, weight + 1):
            without_curr_item = prev[col]
            if col < items[row-1].weight:
                with_curr_item = without_curr_item
            else:
                with_curr_item = prev[col - items[row-1].weight] + items[row-1].value
            curr[col] = max(without_curr_item, with_curr_item)
        prev = curr.copy()
    return curr[-1]


def knapsack_problem_variant_2():
    # TODO: Solve the same problem using O(C) space, where C is the number of weights between 0
    # and w that can be achieved. For example, if the weights are 100, 200, 200, 500, and w = 853, then
    # C = 9, corresponding to the weights 0, 100, 200, 300, 400, 500, 600, 700, 800.
    pass


def knapsack_problem_variant_3():
    # TODO: Solve the fractional knapsack problem. In this formulation the thief can take a fractional
    # part of an item, e.g., by breaking it. Assume the value of a fraction of an item is that fraction times
    # the value of the item.
    pass


def knapsack_problem_variant_4():
    # TODO: In the "divide-the-spoils-fairly" problem, two thieves who have successfully completed
    # a burglary want to know how to divide the stolen items into two groups such that the difference
    # between the value of these two groups is minimized. For example, they may have stolen the clocks
    # in Figure 16.8 on the precedingpa3e, and would like to divide the clocks between them so that the
    # diffurence of the dollar value of the two sets is minimized. For this instance, an optimum split is
    # lA, G, I, M, O, Pl to one thief and the remaining to the other thief. The first set has value $1J79, and
    # the second has value $1180. An equal split is impossible, since the sum of the values of all the clocks
    # is odd. Write a program to solve the divide-the-spoils-fairly problem,
    pass


def knapsack_problem_variant_5():
    # TODO: Solve the divide-the-spoils-fairly problem with the additional constraint that the thieves
    # have the same number of items.
    pass


def knapsack_problem_variant_6():
    # TODO: The US President is electedby the members of the Electoral College. The number of electors
    # per state and Washington, D.C., are given in Table 16.2 on the next page. All electors from each state
    # as well as Washington, D.C., cast their vote for the same candidate. Write a program to determine
    # if a tie is possible in a presidential election with two candidates
    pass


def main():
    print(knapsack_problem(7, [Item(2,2), Item(2,3), Item(3,10)]))
    print(knapsack_problem_iterative(7, [Item(2,2), Item(2,3), Item(3,10)]))
    print(knapsack_problem_variant_1(7, [Item(2,2), Item(2,3), Item(3,10)]))


if __name__ == "__main__":
    main()
