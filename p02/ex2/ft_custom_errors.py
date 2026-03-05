#!/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def custom_errors_test(test_case: str) -> None:
    if test_case == "PlantError":
        try:
            print("Testing PlantError...")
            raise PlantError("The tomato plant is wilting!")

        except PlantError as e:
            print(f"Caught {e.__class__.__name__}: {e}")

    elif test_case == "WaterError":
        try:
            print("Testing WaterError...")
            raise WaterError("Not enough water in the tank!")
        except WaterError as e:
            print(f"Caught {e.__class__.__name__}: {e}")
    elif test_case == "GardenError":
        try:
            print("Testing catching all garden errors...")
            raise PlantError("The tomato plant is wilting!")
        except GardenError as e:
            print(f"Caught a garden error: {e}")
        try:
            raise WaterError("Not enough water in the tank!")
        except GardenError as e:
            print(f"Caught a garden error: {e}")
    else:
        print("Invalid value!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    test_cases = ["PlantError", "WaterError", "GardenError"]
    for case in test_cases:
        custom_errors_test(case)
        print()
    print("All custom error types work correctly!")
