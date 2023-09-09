def nearest_repeated_entries(array):
    latest_index_map, min_distance = {}, float("inf")
    for ind, word in enumerate(array):
        if word in latest_index_map:
            min_distance = min(min_distance, ind - latest_index_map[word])
        latest_index_map[word] = ind
    return min_distance


def main():
    array = ["All", "work", "and", "no", "play", "makes", "for", "no", "work","no", "fun" "and", "no", "results"]
    print(nearest_repeated_entries(array))


if __name__ == "__main__":
    main()
