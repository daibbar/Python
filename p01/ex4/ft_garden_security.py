class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height = height
        self.__age = age

    def __str__(self):
        return (
            f"Current plant: {self.name} ({self.__height}cm, "
            f"{self.__age} days)"
            )

    def set_height(self, height: int) -> str:
        if height < 0:
            return (
                f"Invalid operatin attempted: height {height}cm [REJECTED]\n"
                f"Security: Negative height rejected"
                )
        else:
            self.__height = height
            return (
                f"Height updated: {height}cm [OK]"
                )

    def get_height(self) -> int:
        return self.__height

    def set_age(self, age: int) -> str:
        if age < 0:
            return (
                f"Invalid operatin attempted: age {age}cm [REJECTED]\n"
                f"Security: Negative age rejected"
                )
        else:
            self.__age = age
            return (f"Age updated: {age} days [OK]")

    def get_age(self) -> int:
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 20, 25)
    print(f"Plant created: {rose.name}")
    print(rose.set_height(25))
    print(f"{rose.set_age(30)}\n")
    print(f"{rose.set_height(-5)}\n")
    print(rose)
