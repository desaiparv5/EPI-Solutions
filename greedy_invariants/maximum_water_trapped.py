def maximum_water_trapped(heights):
    left, right = 0, len(heights) - 1
    area = 0
    while left < right:
        area = max(area, (right-left)*min(heights[left],heights[right]))
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return area


def main():
    print(maximum_water_trapped([1,8,6,2,5,4,8,3,7]))


if __name__ == "__main__":
    main()
