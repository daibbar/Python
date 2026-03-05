#!/bin/env python3

def check_temperature(temp_str: str) -> int:
    try:
        temp_int = int(temp_str)
    except ValueError:
        raise ValueError(f"Error: '{temp_str}' is not a valid number")

    if temp_int < 0:
        raise ValueError(f"Error: {temp_str}°C is too cold for plants "
                         f"(min 0°C)")
    elif temp_int > 40:
        raise ValueError(f"Error: {temp_str}°C is too hot for plants "
                         f"(max 40°C)")

    return temp_int


def test_temperature_input(temperature: str) -> None:
    print(f"Testing temperature: {temperature}")
    try:
        print(f"Temperature {check_temperature(temperature)}°C is perfect for "
              f"plants!")
    except Exception as exc:
        print(exc)


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_values = ["25", "abc", "100", "-50"]
    for test in test_values:
        test_temperature_input(test)
        print("")
    print("All tests completed - program didn't crash!")
