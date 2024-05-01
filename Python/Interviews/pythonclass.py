class Car:
    def __init__(self,brand,model):
        self.__brand = brand    # __ in brand makes it private and only accessable in class
        self.model = model
    # getter function 
    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
my_car = Car("Tata", "Nexon")
print(my_car.full_name())
print(my_car.get_brand())



# animal class 
class Animal:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"
class Dog(Animal):
    def __inti__(self,name,age,breed):
        super().__init__(self)
        self.breed = breed

# my_dog = Dog("Molly", 5, "indian")

# print(my_dog.bark())