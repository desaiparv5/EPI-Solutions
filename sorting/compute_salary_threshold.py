def compute_salary_threshold(current_salaries, target_payroll):
    current_salaries.sort()
    unadj_salary = 0
    for ind, salary in enumerate(current_salaries):
        adj_people = len(current_salaries) - ind
        adj_salary_sum = salary * adj_people
        if adj_salary_sum + unadj_salary >= target_payroll:
            return (target_payroll - unadj_salary)/adj_people
        unadj_salary += salary
    return -1


def main():
    current_salaries = [90, 30, 100, 40, 20]
    target_payroll = 210
    print(compute_salary_threshold(current_salaries, target_payroll))


if __name__ == "__main__":
    main()
