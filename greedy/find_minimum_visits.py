import collections
from typing import List


Interval = collections.namedtuple("Interval", ["start", "end"])


def find_minimum_visits(intervals: List[Interval]):
    intervals.sort(key=lambda x: x.end)
    points = [intervals[0].end]
    for interval in intervals[1:]:
        if interval.start <= points[-1] <= interval.end:
            continue
        if interval.start > points[-1]:
            points.append(interval.end)
        if interval.end < points[-1]:
            points[-1] = interval.end
    return points

def find_minimum_visits_variant_1(intervals: List[Interval]):
    # TODO: You are responsible for the security of a castle. The castle has a circular perimeter. A total
    # of n robots Patrol the perimeter .Each robot is responsible for a closed connected subset of the
    # perimeter, i.e., an arc. (The arcs for different robots may overlap.) You want to monitor the robots
    # by installing cameras at the center of the castle that look out to the perimeter. Each camera can look
    # along a ray. To save cost, you would like to minimize the number of cameras.
    pass


def find_minimum_visits_variant_1(intervals: List[Interval]):
    # TODO: There are a number of points in the plane that you want to observe. You are located at the
    # point (0,0). You can rotate about this point, and your field-of-view is a fixed angle. Which direction
    # should you face to maximize the number of visible points?
    pass


def main():
    print(find_minimum_visits([
        Interval(0,3),
        Interval(2,6),
        Interval(3,4),
        Interval(6,9),
    ]))
    print(find_minimum_visits([
        Interval(1,2),
        Interval(2,3),
        Interval(3,4),
        Interval(2,3),
        Interval(3,4),
        Interval(4,5),
    ]))


if __name__ == "__main__":
    main()
