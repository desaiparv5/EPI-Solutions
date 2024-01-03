import typing as t
from collections import Counter


class Person:
    def __init__(self, age, name) -> None:
        self.age = age
        self.name = name
    
    def __repr__(self):
        return f"{self.age} - {self.name}"


def group_by_age(people: t.List[Person]):
    age_count = Counter([x.age for x in people])
    age_offset, offset = {}, 0
    for age, count in age_count.items():
        age_offset[age] = offset
        offset += count

    while age_offset:
        from_age = next(iter(age_offset))
        from_idx = age_offset[from_age]
        to_age = people[from_idx].age
        to_idx = age_offset[to_age]
        people[from_idx], people[to_idx] = people[to_idx], people[from_idx]
        age_count[to_age] -= 1
        if age_count[to_age]:
            age_offset[to_age] = to_idx + 1
        else:
            del age_offset[to_age]


def main():
    people = [Person(12,"a"),Person(13,"b"),Person(12,"c"),Person(12,"d"),Person(13,"e"),Person(14,"f"),Person(13,"g"),Person(13,"h")]
    group_by_age(people)
    print(people)


if __name__ == "__main__":
    main()
