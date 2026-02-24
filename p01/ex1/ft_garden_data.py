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
