import typing as t


class Interval:
    def __init__(self, start, stop) -> None:
        self.start = start
        self.stop = stop
    def __repr__(self):
        return f"({self.start}, {self.stop})"


def union_of_intervals(intervals: t.List[Interval]):
    intervals = sorted(intervals, key=lambda x: x.start)
    result = [intervals[0]]
    curr_index = 1
    while curr_index < len(intervals):
        interval = intervals[curr_index]
        if result[-1].stop < interval.start:
            result.append(interval)
            continue
        result[-1].stop = max(result[-1].stop, interval.stop)
        curr_index += 1
    return result        


def main():
    intervals = [Interval(1,1),Interval(0,3),Interval(3,4),Interval(2,4),Interval(8,11),
                 Interval(13,15),Interval(16,17),Interval(7,8),Interval(12,16),Interval(5,7),
                 Interval(9,11),Interval(12,14)]
    print(union_of_intervals(intervals))


if __name__ == "__main__":
    main()
