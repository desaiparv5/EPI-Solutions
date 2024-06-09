def score_combinations(target, individual_scores):
    combinations = []
    def helper(target, combination, curr_index):
        if target == 0:
            combinations.append(combination)
            return
        if target < 0 or curr_index == len(individual_scores):
            return
        curr_score = individual_scores[curr_index]
        max_combinations = target // curr_score
        for n in range(max_combinations + 1):
            helper(target - curr_score * n, combination + [curr_score] * n, curr_index + 1)
    helper(target, [], 0)
    return combinations


def num_score_combinations_dp(target, individual_scores):
    # space complexity O(len(target) * len(individual_scores))
    # time complexity O(len(target) * len(individual_scores))
    num_combinations_for_score = [[1] + [0] * target for _ in individual_scores]
    for i in range(len(individual_scores)) :
        for j in range(1, target + 1):
            without_this_play = num_combinations_for_score[i - 1][j] if i >= 1 else 0
            with_this_play = num_combinations_for_score[i][j - individual_scores[i]] if j >= individual_scores[i] else 0
            num_combinations_for_score[i][j] = with_this_play + without_this_play
    return num_combinations_for_score[-1][-1]


def num_score_combinations_variant_1(target, individual_scores):
    # space complexity O(len(target))
    # time complexity O(len(target) * len(individual_scores))
    num_combinations_for_score = [1] + [0] * target
    for i in range(len(individual_scores)) :
        for j in range(1, target + 1):
            without_this_play = num_combinations_for_score[j] if i >= 1 else 0
            with_this_play = num_combinations_for_score[j - individual_scores[i]] if j >= individual_scores[i] else 0
            num_combinations_for_score[j] = with_this_play + without_this_play
    return num_combinations_for_score[-1]


def num_score_combinations_variant_2(target, individual_scores):
    # Permutation
    # Write a program that takes a final score and scores for individual plays, and returns the
    # number of sequences of plays that result in the final score. For example, 18 sequences of plays yield
    # a score of 12. Some examples are (2,2,2,3,3), (2,3,2,2,3), (2,3,7), (7,3,2)
    dp = {0: 1}
    for total in range(1, target + 1):
        dp[total] = 0
        for score in individual_scores:
            dp[total] += dp.get(total - score, 0)
    return dp[target]


def num_score_combinations_variant_3():
    # TODO
    # Suppose the final score is given in the form (s,s'), i.e., Team 1 scored s points and Team 2
    # scored s' points. How would you compute the number of distinct scoring sequences which result
    # in this score? For example, if the final score is (6,3) then Team 1 scores 3, Team 2 scores 3, Team 1
    # scores 3 is a scoring sequence which results in this score.
    pass


def num_score_combinations_variant_4():
    # TODO
    # Suppose the final score is (s,s'). How would you compute the maximum number of times
    # the team that lead could have changed? For example, if s = 10 and s' = 6, the lead could have
    # changed 4 times: Team 1 scores 2, then Team 2 scores 3 (lead change), then Team L scores 2 (lead
    # change), then Team 2 scores 3 (lead change), then Team 1 scores 3 (lead change) followed by 3.
    pass


def climb_stairs():
    # TODO
    # You are climbing stairs. You can advance 1 to k steps at a time. Your destination is exactly
    # n steps up. Write a program which takes as inputs n and k and returns the number of ways in which
    # you can get to your destination.
    pass


def main():
    print(score_combinations(7, [2,3,6,7]))
    print(num_score_combinations_variant_1(7, [2,3,6,7]))
    print(num_score_combinations_variant_2(7, [2,3,6,7]))
    print(num_score_combinations_variant_3(6, 6, [2, 6, 7]))
    print(num_score_combinations_dp(7, [2,3,6,7]))

if __name__ == "__main__":
    main()
