def minimum_weight_path_in_triangle(triangle):
    min_weight = [0]
    for row in triangle:
        min_weight = [row[j] + min(min_weight[max(j-1, 0)], min_weight[min(j, len(min_weight) - 1)]) for j in range(len(row))]
    return min(min_weight)


def main():
    triangle = []
    print(minimum_weight_path_in_triangle(triangle))


if __name__ == "__main__":
    main()
