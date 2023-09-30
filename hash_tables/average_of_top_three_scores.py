from collections import defaultdict, namedtuple
from typing import List
from heaps.heap import MinHeap


class Score:
    def __init__(self, score, student_id) -> None:
        self.student_id = student_id
        self.score = score


def average_of_top_three_scores(stream: List[Score]):
    score_map = defaultdict(MinHeap)
    for score in stream:
        score_map[score.student_id].heappush(score.score)
        if len(score_map[score.student_id]) > 3:
            score_map[score.student_id].heappop()
    max_score = 0
    max_score_student = None
    for key, val in score_map.items():
        if len(val) < 3:
            continue
        total = 0
        while val:
            total += val.heappop()
        if (total / 3) > max_score:
            max_score = total / 3
            max_score_student = key
    return max_score_student


def main():
    stream = []
    average_of_top_three_scores(stream)


if __name__ == "__main__":
    main()
