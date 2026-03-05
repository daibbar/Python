#!/bin/env python3


def check_plant_health(plant_name: str, water_level: int, 
                       sunlight_hours: int) -> str:

    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    if 1 < water_level < 10:
        raise ValueError("Water level 15 is too high (max 10)")

    if 2 < sunlight_hours < 12:
        raise ValueError("Sunlight hours 0 is too low (min 2)")

    return (f"Plant {plant_name} is healthy!")


def test_plant_checks():
    pass