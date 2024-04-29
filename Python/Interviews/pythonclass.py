class Animal:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"
class Dog(Animal):
    def __inti__(self):
        super().__init__(self)

my_dog = Dog("Molly", 5)

print(my_dog.bark())
