def gasup_problem(gallons, distances, mpg):
    city = 0
    remaining_gallons = 0
    surplus = 0
    for i in range(len(gallons)):
        remaining_gallons += gallons[i] - distances[i] // mpg
        surplus += gallons[i] - distances[i] // mpg
        if surplus < 0:
            city = i + 1
            surplus = 0
    return city if remaining_gallons >= 0 else -1


def main():
    gallons = [2,3,4]
    distances = [3,4,3]
    mpg = 1
    # print(gasup_problem(gallons, distances, mpg))
    gallons = [1,2,3,4,5]
    distances = [3,4,5,1,2]
    # print(gasup_problem(gallons, distances, mpg))
    gallons = [3,1,1]
    distances = [1,2,2]
    print(gasup_problem(gallons, distances, mpg))


if __name__ == "__main__":
    main()
