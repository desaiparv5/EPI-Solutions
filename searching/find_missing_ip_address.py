import itertools


TOTAL_BITS = 4


def find_missing_ip_address(stream):
    num_bucket = 1 << (TOTAL_BITS // 2)
    counter = [0] * num_bucket

    stream, stream_copy = itertools.tee(stream)

    for x in stream:
        upper_part_x = x >> (TOTAL_BITS // 2)
        counter[upper_part_x] += 1
    
    bucket_capacity = 1 << (TOTAL_BITS // 2)
    candidate_bucket = next(i for i, c in enumerate(counter) if c < bucket_capacity)
    candidates = [0] * bucket_capacity
    stream = stream_copy
    for x in stream_copy:
        upper_part_x = x >> (TOTAL_BITS // 2)
        if upper_part_x == candidate_bucket:
            lower_part_x = ((1 << (TOTAL_BITS // 2)) - 1) & x
            candidates[lower_part_x] = 1
    for i, v in enumerate(candidates):
        if v == 0:
            return candidate_bucket << (TOTAL_BITS // 2) | i


def main():
    stream = [0,1,2,3,4,5,6,7,8,9,10,12,13,14,15]
    print(find_missing_ip_address(stream))


if __name__ == "__main__":
    main()
