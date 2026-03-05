#!/usr/bin/env python3

if __name__ == "__main__":
    name = "Rose"
    height = 25
    age = 30

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days", end="\n\n")
    print("=== End of Program ===")
#!/usr/bin/env python3

class Plant:
    name: str
    height: int
    age: int


if __name__ == "__main__":
    rose: Plant = Plant()
    rose.name = "Rose"
    rose.age = 30
    rose.height = 25

    sunflower: Plant = Plant()
    sunflower.name = "Sunflower"
    sunflower.age = 45
    sunflower.height = 80

    cactus: Plant = Plant()
    cactus.name = "Cactus"
    cactus.age = 120
    cactus.height = 15

    plants = [rose, sunflower, cactus]
    print("=== Garden Plant Registry ===")
    for flower in plants:
        print(f"{flower.name}: {flower.height}cm, {flower.age} days old")
#!/usr/bin/env python3

class Plant:
    name: str
    height: int
    plant_age: int

    def age(self) -> None:
        self.plant_age += 1

    def grow(self) -> None:
        self.height += 1

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm, {self.plant_age} days old"

    def get_info(self) -> int:
        return self.height


if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose.plant_age = 30
    rose.height = 25

    sunflower = Plant()
    sunflower.name = "sunflower"
    sunflower.plant_age = 45
    sunflower.height = 80

    cactus = Plant()
    cactus.name = "Cactus"
    cactus.plant_age = 120
    cactus.height = 15

    plants = [rose, sunflower, cactus]
    print("=== Day 1 ===")
    for flower in plants:
        print(flower)

    plants_init_state = [flower.get_info() for flower in plants]
    for day in range(6):
        for flower in plants:
            flower.grow()
            flower.age()

    print("=== Day 7 ===")
    i = 0
    for flower in plants:
        print(flower)
        flower_current_state = flower.get_info() - plants_init_state[i]
        print(f"Growth this week: +{flower_current_state}cm", end="\n\n")
        i += 1
#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)

    plants = [rose, oak, cactus, sunflower, fern]
    plants_counter = 0
    print("=== Plant Factory Output ===")
    for flower in plants:
        print(flower)
        plants_counter += 1
    print(f"\nTotal plants created: {plants_counter}")
#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    def __str__(self):
        return (
            f"Current plant: {self.name} ({self._height}cm, "
            f"{self._age} days)"
            )

    def set_height(self, height: int) -> str:
        if height < 0:
            return (
                f"Invalid opeartion attempted: height {height}cm [REJECTED]\n"
                f"Security: Negative height rejected"
                )
        else:
            self._height = height
            return (
                f"Height updated: {height}cm [OK]"
                )

    def get_height(self) -> int:
        return self._height

    def set_age(self, age: int) -> str:
        if age < 0:
            return (
                f"Invalid opeartion attempted: age {age}cm [REJECTED]\n"
                f"Security: Negative age rejected"
                )
        else:
            self._age = age
            return (f"Age updated: {age} days [OK]")

    def get_age(self) -> int:
        return self._age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 20, 25)
    print(f"Plant created: {rose.name}")
    print(rose.set_height(25))
    print(f"{rose.set_age(30)}\n")
    print(f"{rose.set_height(-5)}\n")
    print(rose)

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
#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, growth: int) -> str:
        self.height += growth
        return (f"{self.name} grew {growth}cm")

    def __str__(self) -> str:
        return (
            f"- {self.name}: {self.height}cm"
        )


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        return ("(blooming)")

    def __str__(self) -> str:
        return (
            f"{super().__str__()}, {self.color} flowers {self.bloom()}"
        )


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str,
                 prize_points: int):
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def __str__(self) -> str:
        return (
            f"{super().__str__()}, Prize points: {self.prize_points}"
        )


class Garden():
    def __init__(self, garden_owner: str, plants: list[Plant]) -> None:
        self.name: str = garden_owner
        self.plants: list = plants
        self.total_plants_height: int = 0
        self.plants_total: int = 0
        self.total_regular_plants: int = 0
        self.total_flowering_plants: int = 0
        self.total_prize_flowers: int = 0


class GardenManager:
    _gardens: list[Garden] = []

    def __init__(self, garden_manager_name: str):
        self.garden_manager_name = garden_manager_name

    def create_garden_network(cls, gardens: list[Garden]):
        for garden in gardens:
            cls._gardens += [garden]
        return (cls._gardens)
    create_garden_network = classmethod(create_garden_network)

    def add_garden(cls, garden: Garden) -> None:
        cls._gardens += [garden]
    add_garden = classmethod(add_garden)

    def get_gardens(cls) -> list[Garden]:
        return cls._gardens
    get_gardens = classmethod(get_gardens)

    def garden_total(cls):
        garden_total = 0
        for _ in cls._gardens:
            garden_total += 1
        return garden_total
    garden_total = classmethod(garden_total)

    def add_plant(garden: Garden, plant: Plant) -> str:
        garden.plants += [plant]
        garden.total_plants_height += plant.height
        garden.plants_total += 1

        if plant.__class__.__name__ == "Plant":
            garden.total_regular_plants += 1
        elif plant.__class__.__name__ == "PrizeFlower":
            garden.total_prize_flowers += 1
        elif plant.__class__.__name__ == "FloweringPlant":
            garden.total_flowering_plants += 1
        return (f"Added {plant.name} to {garden.name}")
    add_plant = staticmethod(add_plant)

    def show_plants(garden: Garden) -> None:
        for plant in garden.plants:
            print(plant)
    show_plants = staticmethod(show_plants)

    class GardenStats:
        def current_height(garden: Garden) -> int:
            current_height: int = 0
            for plant in garden.plants:
                current_height += plant.height
            return (current_height)
        current_height = staticmethod(current_height)

        def total_prize_points(garden: Garden) -> int:
            total_points: int = 0
            for plant in garden.plants:
                if plant.__class__.__name__ == "PrizeFlower":
                    total_points += plant.prize_points
            return total_points
        total_prize_points = staticmethod(total_prize_points)

        def total_growth(garden: Garden) -> int:
            return (GardenManager.GardenStats.current_height(garden)
                    - garden.total_plants_height)
        total_growth = staticmethod(total_growth)

        def garden_height_test(garden: Garden) -> bool:
            result: bool = True
            for plant in garden.plants:
                if plant.height < 0:
                    result = False
            return result
        garden_height_test = staticmethod(garden_height_test)

        def garden_score(garden: Garden) -> int:
            return (
                    GardenManager.GardenStats.current_height(garden)
                    + garden.total_regular_plants * 10
                    + garden.total_flowering_plants * 10
                    + garden.total_prize_flowers * 10
                    + GardenManager.GardenStats.total_prize_points(garden)
                    )
        garden_score = staticmethod(garden_score)

        def garden_plant_types(garden: Garden) -> str:
            return (
                    f"Plant types: {garden.total_regular_plants} regular, "
                    f"{garden.total_flowering_plants} flowering, "
                    f"{garden.total_prize_flowers} prize flowers"
            )
        garden_plant_types = staticmethod(garden_plant_types)

    def generate_report(cls, garden: Garden) -> None:
        print(format_garden_title(garden.name))
        print("Plants in garden:")
        cls.show_plants(garden)
        print(f"\nplants added: {garden.plants_total}, "
              f"Total growth: {cls.GardenStats.total_growth(garden)}cm\n")
        print(f"{cls.GardenStats.garden_plant_types(garden)}")
        print(f"Height validation test: "
              f"{cls.GardenStats.garden_height_test(garden)}\n")
    generate_report = classmethod(generate_report)


def format_garden_title(name: str) -> str:
    return (f"=== {name}'s Garden Report ===")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    alice_garden = Garden("Alice", [])
    bob_garden = Garden("Bob", [])

    oak_tree = Plant("Oak Tree", 100, 1000)
    rose = FloweringPlant("Rose", 25, 30, "red")
    sunflower = PrizeFlower("Sunflower", 50, 11, "yellow", 10)
    alice_plants = [oak_tree, rose, sunflower]
    for plant in alice_plants:
        print(GardenManager.add_plant(alice_garden, plant))

    narcissus = PrizeFlower("Narcissus", 60, 20, "White", 22)
    GardenManager.add_plant(bob_garden, narcissus)

    gardens = [alice_garden, bob_garden]
    garden_network = GardenManager.create_garden_network(gardens)

    print("\nAlice is helping all plants grow...")
    for plant in alice_plants:
        print(plant.grow(1))
    print("")

    GardenManager.generate_report(alice_garden)

    print(f"Garden scores - {alice_garden.name}: "
          f"{GardenManager.GardenStats.garden_score(alice_garden)}, "
          f"{bob_garden.name}: "
          f"{GardenManager.GardenStats.garden_score(bob_garden)}")
    print(f"Total gardens managed: {GardenManager.garden_total()}")
