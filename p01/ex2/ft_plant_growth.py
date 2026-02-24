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
