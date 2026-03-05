#!/bin/env python3

def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"watering {plant}")

    except ValueError as e:
        print(f"Error: {e}")
        print(repr(e))
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    try:
        print("Testing normal watering...")
        water_plants(["tomato", "lettuce", "carrots"])
        print("Watering completed successfully!\n")

        print("Testing with error...")
        water_plants(["tomato", None])
        print()
    except Exception as e:
        print(f"Unexpected error has occured!: {e}\n")

    finally:
        print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
