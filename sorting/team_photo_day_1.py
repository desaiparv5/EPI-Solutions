from collections import namedtuple
from typing import List


Player = namedtuple("Player", ("height"))

class Team:
    def __init__(self, players: List[Player]) -> None:
        self.players = players


def is_team_photo_possible(team_a: Team, team_b: Team):
    return all([a < b for a, b in zip(sorted(team_a.players, key=lambda x: x.height), sorted(team_b.players, key=lambda x: x.height))])


def main():
    team_a = Team([Player(2), Player(1),Player(6),Player(3),Player(5)])
    team_b = Team([Player(2),Player(3),Player(4),Player(7),Player(7)])
    print(is_team_photo_possible(team_a, team_b))


if __name__ == "__main__":
    main()
