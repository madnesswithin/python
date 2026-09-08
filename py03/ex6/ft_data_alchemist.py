#!/usr/bin/env python3
import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    players = ["Alice", "bob", "Charlie", "dylan", "Emma",
               "Gregory", "john", "kevin", "Liam"]
    print(f"Initial list of players: {players}")

    all_capitalized = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_capitalized}")

    already_capitalized = [name for name in players if name.istitle()]
    print(f"New list of capitalized names only: {already_capitalized}")

    scores = {name: random.randint(0, 999) for name in all_capitalized}
    print(f"Score dict: {scores}")

    average = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {average}")

    high_scores = {name: score for name, score in scores.items()
                   if score > average}
    print(f"High scores: {high_scores}")
