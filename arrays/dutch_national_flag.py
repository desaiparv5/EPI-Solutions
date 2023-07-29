"""Dutch national flag problem"""
from enum import IntEnum
from time import process_time_ns
import random
import string


class Color(IntEnum):
    RED = 1
    WHITE = 2
    BLUE = 3
    ORANGE = 4

    def __repr__(self):
        return f'{self.name}'


def dutch_national_flag_single_iter(arr):
    # Standard Dutch National Flag Problem
    low = -1
    equal = 0
    high = len(arr) - 1
    while equal <= high:
        if arr[equal] < Color.WHITE:
            low += 1
            arr[equal], arr[low] = arr[low], arr[equal]
            equal += 1
        elif arr[equal] == Color.WHITE:
            equal += 1
        else:
            arr[equal], arr[high] = arr[high], arr[equal]
            high -= 1


def sort_colors_together(arr):
    # Sort same colors together
    if len(arr) <= 2:
        return
    low = -1
    low_key = arr[0]
    medium = 0
    med_key = None
    high = len(arr) - 1

    while medium <= high:
        if arr[medium] == low_key:
            low += 1
            arr[low], arr[medium] = arr[medium], arr[low]
            medium += 1
        elif not med_key:
            med_key = arr[medium]
            medium += 1
        elif med_key and arr[medium] == med_key:
            medium += 1
        else:
            arr[medium], arr[high] = arr[high], arr[medium]
            high -= 1


def dutch_national_flag_four_colors(arr):
    k1, k2, k3, k4 = 0, 0, 0, len(arr) - 1
    while k3 <= k4:
        if arr[k3] == Color.RED:
            arr[k1], arr[k3] = arr[k3], arr[k1]
            k1 += 1
            k3 += (1 if k2 >= k3 else 0)
            k2 += (1 if k1 > k2 else 0)
        elif arr[k3] == Color.WHITE:
            arr[k3], arr[k2] = arr[k2], arr[k3]
            k2 += 1
            k3 += 1
        elif arr[k3] == Color.BLUE:
            k3 += 1
        elif arr[k3] == Color.ORANGE:
            arr[k3], arr[k4] = arr[k4], arr[k3]
            k4 -= 1


class Car:
    def __init__(self, name, is_running):
        self.name = name
        self.is_running = is_running
    
    def __repr__(self) -> str:
        return f"{self.name} - {self.is_running}"


def sort_cars_based_on_running_state(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        if arr[low].is_running:
            arr[low], arr[high] = arr[high], arr[low]
            high -= 1
        else:
            low += 1


def sort_cars_based_on_running_state_preserve_runnning_cars_order(arr):
    num_running = 0
    total_cars = len(arr)

    for car in arr:
        if car.is_running: num_running += 1
    
    curr = 0
    running_index = num_running
    while curr < (total_cars - num_running):
        if arr[curr].is_running:
            arr[running_index], arr[curr] = arr[curr], arr[running_index]
            running_index += 1
        else:
            curr += 1


def main():
    test_arr_dutch = [random.choice([Color.BLUE, Color.RED, Color.WHITE]) for _ in range(10)]

    arr = test_arr_dutch.copy()
    start_time = process_time_ns()
    dutch_national_flag_single_iter(arr)
    print(f"Time taken: {(process_time_ns() - start_time)}")

    arr = test_arr_dutch.copy()
    start_time = process_time_ns()
    sort_colors_together(arr)
    print(f"Time taken: {(process_time_ns() - start_time)}")

    test_arr_dutch_four_colors = [random.choice([Color.BLUE, Color.RED, Color.WHITE, Color.ORANGE]) for _ in range(10)]
    arr = test_arr_dutch_four_colors.copy()
    start_time = process_time_ns()
    dutch_national_flag_four_colors(arr)
    print(f"Time taken: {(process_time_ns() - start_time)}")

    test_obj_arr = [Car(name=''.join(random.choices(string.ascii_lowercase, k=7)), is_running=random.choice([True, False])) for _ in range(10)]

    arr = test_obj_arr.copy()
    start_time = process_time_ns()
    sort_cars_based_on_running_state(arr)
    print(f"Time taken: {(process_time_ns() - start_time)}")

    arr = test_obj_arr.copy()
    start_time = process_time_ns()
    # sort_cars_based_on_running_state_preserve_runnning_cars_order(arr)
    print(f"Time taken: {(process_time_ns() - start_time)}")


if __name__ == "__main__":
    main()
