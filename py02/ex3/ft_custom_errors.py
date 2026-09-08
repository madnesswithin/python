#!/usr/bin/env python3


class GardenError(Exception):
    """Base exception for garden-related problems."""

    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Exception for problems with plants."""

    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    """Exception for problems with watering."""

    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_plant(plant_name: str) -> None:
    if plant_name == "wilted_tomato":
        raise PlantError("The tomato plant is wilting!")


def check_water(tank_level: int) -> None:
    if tank_level <= 0:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()

    print("Testing PlantError...")
    try:
        check_plant("wilted_tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()

    print("Testing WaterError...")
    try:
        check_water(0)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()

    print("Testing catching all garden errors...")
    try:
        check_plant("wilted_tomato")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water(0)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print()

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
