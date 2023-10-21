import typing as t
from collections import namedtuple


Interval = namedtuple("Interval", ["start", "end"])


def merging_intervals(intervals: t.List[Interval], new_interval: Interval):
    curr_index = 0
    result = []
    while curr_index < len(intervals) and new_interval.start > intervals[curr_index].end:
        result.append(intervals[curr_index])
        curr_index += 1
    while curr_index < len(intervals) and new_interval.end >= intervals[curr_index].start:
        new_interval = Interval(
            min(new_interval.start, intervals[curr_index].start), 
            max(new_interval.end, intervals[curr_index].end)
        )
        curr_index += 1
    return result + [new_interval] + intervals[curr_index:]


def main():
    intervals = [Interval(-4,-1), Interval(0,2), Interval(3,6), Interval(7,9), Interval(11,12), Interval(14,17)]
    new_interval = Interval(1, 8)
    print(merging_intervals(intervals, new_interval))


if __name__ == "__main__":
    main()
