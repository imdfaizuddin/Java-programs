class Car:
    def __init__(self,brand,model):
        self.__brand = brand    # __ in brand makes it private and only accessable in class
        self.model = model
    # getter function #Encapsulation
    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    #Polymorphism
    def fuel_type(self):
        return "Petrol or Diesel"
    
# ElectricCar inheriting Car class 
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def batteryInfo(self):
        return self.battery_size
    #Polymorphism
    def fuel_type(self):
        return "Electric charge"

my_car = ElectricCar("Tata", "Nexon", "10kWh")
# print(my_car.__brand)  This won't work because __brand is private
# print(my_car.full_name())
# print(my_car.get_brand())
# print(my_car.batteryInfo())
car1 = Car("Tata","Safari")
print(car1.fuel_type())     #Petrol or Diesel
print(my_car.fuel_type())   #Electric charge



# animal class 
class Animal:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"
class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed = breed

my_dog = Dog("Molly", 5, "indian")

# print(my_dog.bark())