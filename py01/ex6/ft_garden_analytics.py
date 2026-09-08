#!/usr/bin/env python3


class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def record_grow(self) -> None:
            self._grow_count += 1

        def record_age(self) -> None:
            self._age_count += 1

        def record_show(self) -> None:
            self._show_count += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_count} grow, "
                  f"{self._age_count} age, {self._show_count} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self.stats = Plant.Stats()
        self.set_height(height, announce=False)
        self.set_age(age, announce=False)

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

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
        self.stats.record_grow()

    def plant_age(self) -> None:
        self._age = self._age + 1
        self.stats.record_age()

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")
        self.stats.record_show()


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
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def record_shade(self) -> None:
            self._shade_count += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade_count} shade")

    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.stats: "Tree.Stats" = Tree.Stats()

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of "
              f"{round(self.get_height(), 1)}cm long and "
              f"{round(self.trunk_diameter, 1)}cm wide.")
        self.stats.record_shade()

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


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


def display_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> "
          f"{Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year? -> "
          f"{Plant.is_older_than_a_year(400)}")

    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_plant_stats(rose)

    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)

    print()
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.plant_age()
    sunflower.bloom()
    sunflower.show()
    display_plant_stats(sunflower)

    print()
    print("=== Anonymous")
    mystery = Plant.create_anonymous()
    mystery.show()
    display_plant_stats(mystery)
