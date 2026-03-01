#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        return (f"{self.height}cm, {self.age} days")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        return (f"{self.name} is blooming beautifully!")

    def __str__(self) -> str:
        return (f"{self.name} (Flower): "
                f"{super().__str__()}, {self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade_area = (3.14 * ((self.trunk_diameter / 10) ** 2))
        return (f"{self.name} provides {shade_area} square meters of shade")

    def __str__(self) -> str:
        return (f"{self.name} (Tree): "
                f"{super().__str__()}, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def produce_shade(self, shade_area: int) -> None:
        return (f"{self.name} provides {shade_area} square meters of shade")

    def __str__(self) -> str:
        return (f"{self.name} (Vegetable): "
                f"{super().__str__()}, {self.harvest_season} harvest")

    def nutrition(self):
        return (f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    rose = Flower("Rose", 25, 30, "red")
    narcissus = Flower("Narcissus", 75, 20, "white")

    oak = Tree("Oak", 500, 1825, 50)
    maple = Tree("Maple", 3000, 6000, 70)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    lettuce = Vegetable("Lettuce", 90, 100, "spring", "vitamin A")

    plants = [rose, narcissus, oak, maple, tomato, lettuce]
    print("=== Garden Plant Types ===")
    index = 0
    for plant in plants:
        print(plant)
        if (index <= 1):
            print(f"{plant.bloom()}\n")
        elif (index <= 3):
            print(f"{plant.produce_shade()}\n")
        else:
            print(f"{plant.nutrition()}\n")
        index += 1
