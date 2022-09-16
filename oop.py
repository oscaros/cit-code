# class age:
#     def __init(self, age ):
#         #self.age = self.getAge(age)
#         self.age = age
    
#     def getAge(self, age):
#         howOld= 2022 - age
#         return howOld

# howAged = age()
# print(howAged.getAge(31))


class Parrot:
class Animal:
class Car:
    def __init__(self, model, color, brand, price):
        self.model = model
        self.color = color
        self.brand = brand
        self.price = price

    def move(self, direction, speed):
        print(f"{self.brand} is moving in {direction} direction at a speed of {speed} km/h")

    def stop(self):
        print(f"{self.brand} has stopped")

    def update_price(self, price):
        self.price = price
        print(f"The new price is {self.price}")

import time


car_bmw = Car("X5", "Black", "BMW", 50000.0)
# benz = Car(model, color, brand, price)
# nissan = Car(model, color, brand, price)

print(f"My car is a {car_bmw.color} {car_bmw.model} {car_bmw.brand} that costs {car_bmw.price}")

car_bmw.move("North", 50)
car_bmw.stop()
car_bmw.update_price(600000.00)
print(car_bmw.price)

