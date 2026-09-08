#!/usr/bin/env python3


class GardenError(Exception):
    """Base exception for garden-related problems."""

    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Exception for problems with plants."""

    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if not plant_name[0:1].isupper():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plant_names: list[str]) -> None:
    try:
        print("Opening watering system")
        for name in plant_names:
            water_plant(name)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print()

    print("Testing valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])
    print()

    print("Testing invalid plants...")
    test_watering_system(["Tomato", "lettuce", "Carrots"])
    print()

    print("Cleanup always happens, even with errors!")
