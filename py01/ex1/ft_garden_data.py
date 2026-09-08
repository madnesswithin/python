#!/usr/bin/env python3


class Plant:
    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    red_plant = Plant()
    red_plant.name = "Rose"
    red_plant.height = 25
    red_plant.age = 30
    fav_plant = Plant()
    fav_plant.name = "Sunflower"
    fav_plant.height = 80
    fav_plant.age = 45
    prickly_plant = Plant()
    prickly_plant.name = "Cactus"
    prickly_plant.height = 15
    prickly_plant.age = 120
    red_plant.show()
    fav_plant.show()
    prickly_plant.show()
