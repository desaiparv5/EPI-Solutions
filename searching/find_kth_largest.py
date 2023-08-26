import itertools
import operator
import typing


def quickselect_kth(array, k, comp):
    def partition(left, right):
        pivot = array[right]
        new_pivot = left
        for i in range(left, right):
            if comp(pivot, array[i]):
                array[new_pivot], array[i] = array[i], array[new_pivot]
                new_pivot += 1
        array[new_pivot], array[right]= array[right], array[new_pivot]
        return new_pivot
    
    left, right = 0, len(array) - 1
    while left <= right:
        new_pivot = partition(left, right)
        if new_pivot == k - 1:
            return array[new_pivot]
        elif new_pivot > k - 1:
            right = new_pivot - 1
        else:
            left = new_pivot + 1


def find_kth_largest_quickselect(array, k):
    return quickselect_kth(array, k, operator.lt)


def find_kth_smallest_quickselect(array, k):
    return quickselect_kth(array, k, operator.gt)


def find_median(array):
    if len(array) % 2:
        return find_kth_largest_quickselect(array, len(array) // 2 + 1)
    left = find_kth_smallest_quickselect(array, len(array) // 2)
    right = find_kth_largest_quickselect(array, len(array) // 2)
    return (left + right) / 2


class Building:
    def __init__(self, distance, residents) -> None:
        self.distance = distance
        self.residents = residents


def place_mailbox(buildings_array: typing.List[Building]):
    """A number of apartment buildings are coming up on a new street. The postal service
    wants to place a single mailbox on the street. Their objective is to minimize the total distance
    that residents have to walk to collect their mail each day. (Different buildings may have different
    numbers of residents.)
    Devise an algorithm that computes where to place the mailbox so as to minimize the total
    distance, that residents travel to get to the mailbox. Assume the input is specified as an array of
    building objects, where each building object has a field indicating the number of residents in that
    building, and a field indicating the building's distance from the start of the street.
    """
    buildings_array.sort(key=lambda x: x.distance)

    total_residents = [res for res in itertools.accumulate(buildings_array, func = lambda x, y: x + y.residents, initial=0)]
    total_residents_rev = [res for res in itertools.accumulate(buildings_array[::-1], func = lambda x, y: x + y.residents, initial=0)]
    
    for i in range(1, len(total_residents) - 1):
        total_residents[i] = total_residents[i-1] + total_residents[i] * (buildings_array[i].distance - buildings_array[i-1].distance)
        total_residents_rev[i] = total_residents_rev[i-1] + total_residents_rev[i] * (buildings_array[-i].distance - buildings_array[-i-1].distance)

    min_distance, min_distance_index = float("inf"), 0
    for i in range(len(buildings_array)):
        if min_distance > (total_residents[i] + total_residents_rev[-i-2]):
            min_distance = total_residents[i] + total_residents_rev[-i-2]
            min_distance_index = i
    return min_distance_index


def main():
    array = [1, 7, 2, 5, 10, 11, 11, 13, 6, 9]
    k = 9
    print(find_kth_largest_quickselect(array, 3))
    print(find_kth_smallest_quickselect(array, k))
    print(find_median(array))

    buildings = [Building(2, 10), Building(1,30), Building(10,30)]
    print(place_mailbox(buildings))

if __name__ == "__main__":
    main()
