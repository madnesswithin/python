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
    print("=== Plant Factory Output ===")
    red_plant = Plant("Rose", 25.0, 30)
    print("Created: ", end="")
    red_plant.show()
    tree_plant = Plant("Oak", 200.0, 365)
    print("Created: ", end="")
    tree_plant.show()
    prickly_plant = Plant("Cactus", 5.0, 90)
    print("Created: ", end="")
    prickly_plant.show()
    fav_plant = Plant("Sunflower", 80.0, 45)
    print("Created: ", end="")
    fav_plant.show()
    whispy_plant = Plant("Fern", 15.0, 120)
    print("Created: ", end="")
    whispy_plant.show()
