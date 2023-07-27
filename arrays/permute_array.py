def permute_array(permutation, arr):
    for i in range(len(permutation)):
        next = i
        while permutation[next] != -1:
            arr[i], arr[permutation[next]] = arr[permutation[next]], arr[i]
            # next_char, arr[permutation[next]] = arr[permutation[next]], next_char
            temp = permutation[next]
            permutation[next] = -1
            next = temp


def permute_array_2(permutation, arr):
    def cyclic_permutation(start):
        perm = start
        temp = arr[start]
        while True:
            next_perm = permutation[perm]
            next_temp = arr[next_perm]
            arr[next_perm] = temp
            perm = next_perm
            temp = next_temp

            if perm == start:
                break
    
    for i in range(len(permutation)):
        is_min = True
        j = permutation[i]

        while j != i:
            if j < i:
                is_min = False
                break
            j = permutation[j]
        
        if is_min:
            cyclic_permutation(i)


def inverse_permutation(permutation, array):
    raise NotImplementedError


def main():
    array = ['a','b','c','d','e']
    permutation = [2, 1, 0, 3, 4]
    # permute_array(permutation, array)
    permute_array_2(permutation, array)
    print(array)
# [d, b, a, c, e]

if __name__ == "__main__":
    main()
