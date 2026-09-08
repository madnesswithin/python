#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height, announce=False)
        self.set_age(age, announce=False)

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float, announce: bool = True) -> None:
        if height < 0:
            print(f"{self.name}: Error, height cannot be negative.")
            print("Height update rejected.")
        else:
            self._height = height
            if announce:
                print(f"Height updated: {round(height, 1)}cm")

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int, announce: bool = True) -> None:
        if age < 0:
            print(f"{self.name}: Error, age cannot be negative.")
            print("Age update rejected.")
        else:
            self._age = age
            if announce:
                print(f"Age updated: {age} days old")

    def grow(self) -> None:
        self._height = self._height + 0.8

    def plant_age(self) -> None:
        self._age = self._age + 1

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    red_plant = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    red_plant.show()
    red_plant.set_height(25.0)
    red_plant.set_age(30)
    red_plant.set_height(-5.0)
    red_plant.set_age(-10)
    print("Current state: ", end="")
    red_plant.show()
