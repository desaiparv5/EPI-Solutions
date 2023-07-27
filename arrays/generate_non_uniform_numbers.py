import random


def non_uniform_random_element(values, probabilities):
    if not len(probabilities):
        raise Exception("Empty values")

    sum_probabilities = [0] * len(probabilities)
    sum_probabilities[0] = probabilities[0]
    i = 1
    while i < len(probabilities):
        sum_probabilities[i] += sum_probabilities[i-1] + probabilities[i]
        i += 1

    if not sum_probabilities[-1] == 1:
        raise Exception("Probabilities not equal to 1")

    random_prob = random.random()

    curr_index = 0
    while curr_index < len(probabilities):
        if probabilities[curr_index] < random_prob: break
        curr_index += 1
    
    return values[curr_index - 1]
    

def main():
    values = [2, 4]
    probabilities = [0.9, 0.1]
    for _ in range(10):
        print(non_uniform_random_element(values, probabilities))


if __name__ == "__main__":
    main()
