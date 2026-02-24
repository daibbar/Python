
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age


p = Person(25)
print(p.age)
p.age = 30
