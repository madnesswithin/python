#!/usr/bin/env python3
import random


ACHIEVEMENTS = [
    "Crafting Genius", "Strategist", "World Savior", "Speed Runner",
    "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable",
    "First Steps", "Collector Supreme", "Untouchable", "Sharp Mind",
    "Boss Slayer", "Hidden Path Finder",
]


def gen_player_achievements() -> set:
    count = random.randint(5, 9)
    return set(random.sample(ACHIEVEMENTS, count))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")

    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")

    print()
    all_achievements: set = set()
    for achievements in players.values():
        all_achievements = all_achievements.union(achievements)
    print(f"All distinct achievements: {all_achievements}")

    print()
    common = all_achievements
    for achievements in players.values():
        common = common.intersection(achievements)
    print(f"Common achievements: {common}")

    print()
    for name, achievements in players.items():
        others: set = set()
        for other_name, other_achievements in players.items():
            if other_name != name:
                others = others.union(other_achievements)
        only_mine = achievements.difference(others)
        print(f"Only {name} has: {only_mine}")

    print()
    all_possible = set(ACHIEVEMENTS)
    for name, achievements in players.items():
        missing = all_possible.difference(achievements)
        print(f"{name} is missing: {missing}")
