#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
# test with a valid number, like "27" -- should succeed
    try:
        print("Input data is '27'")
        temp = input_temperature("27")
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()
# test with invalid string, like "twenty"
# -- failed, catch exception and print error
    try:
        print("Input data is 'twenty'")
        temp = input_temperature("twenty")
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print()
    print("All tests completed - program did not crash!")


if __name__ == "__main__":
    test_temperature()
