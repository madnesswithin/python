#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height = self.height + 0.8

    def plant_age(self) -> None:
        self.age = self.age + 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    red_plant = Plant("Rose", 25.0, 30)
    red_plant.show()
    beginning_height = red_plant.height
    for day in range(1, 8):
        red_plant.grow()
        red_plant.plant_age()
        print(f"=== Day {day} ===")
        red_plant.show()
    growth = red_plant.height - beginning_height
    print(f"Rose grew {round(growth, 1)}cm this week.")
