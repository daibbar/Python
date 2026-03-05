#!/bin/env python3

def garden_operations(operation: str) -> None:
    if operation == "value":
        int("abc")
    elif operation == "zero":
        5 / 0
    elif operation == "file":
        open("missing.txt", "r")
    elif operation == "key":
        d = {}
        d["missing_plant"]


def test_error_types() -> None:
    print("Testing Valuerror...")
    try:
        garden_operations("value")
    except ValueError as e:
        print(f"Caught {e.__class__.__name__}: {e}\n")

    print("Testing ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError as e:
        print(f"Caught {e.__class__.__name__}: {e}\n")

    print("Testing FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError as e:
        print(f"Caught {e.__class__.__name__}: No such file '{e.filename}'\n")

    print("Testing KeyError...")
    try:
        garden_operations("key")
    except KeyError as e:
        print(f"Caught {e.__class__.__name__}: {e}\n")

    print("Testing multiple errors together...")
    multiple_errors = ["value", "zero"]
    for error in multiple_errors:
        try:
            garden_operations(error)
        except (ValueError, ZeroDivisionError):
            continue
    print("Caught an error, but program continues!\n")


if __name__ == "__main__":
    try:
        print("=== Garden Error Types Demo ===\n")
        test_error_types()
    except Exception as e:
        print(f"Unexpected error has occured!: {e}")
    print("All error types tested successfully!")
