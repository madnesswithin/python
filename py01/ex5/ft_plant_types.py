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


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of "
              f"{round(self.get_height(), 1)}cm long and "
              f"{round(self.trunk_diameter, 1)}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk Diameter: {round(self.trunk_diameter, 1)}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int = 0) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def grow(self) -> None:
        self.set_height(self.get_height() + 2.1, announce=False)
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest Season: {self.harvest_season}")
        print(f" Nutritional Value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    pretty_flower = Flower("Rose", 15.0, 10, "Wine red")
    pretty_flower.show()
    print("[Time to bloom!]")
    pretty_flower.bloom()
    pretty_flower.show()
    print("=== Tree")
    big_tree = Tree("Oak", 200.0, 365, 5.0)
    big_tree.show()
    print("[Provide shade for the garden]")
    big_tree.produce_shade()
    print("=== Vegetable")
    tasty_veggie = Vegetable("Tomato", 5.0, 10, "April")
    tasty_veggie.show()
    print("[Nurturing the veggie to grow and age for 20 days]")
    for day in range(1, 21):
        tasty_veggie.grow()
        tasty_veggie.plant_age()
    tasty_veggie.show()
