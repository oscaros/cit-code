from re import X


nested_list = [["apples", "mangoes"], 2, "Oscar"]

print(nested_list[0][1])
print(nested_list[1])
print(nested_list[-1])

my_list = ["p","y", "t", "h", "o", "n"]
print(my_list[2:4])
print(my_list[2:])
print(my_list[0:])
print(my_list[:])

my_list[0] = "X"
print(my_list[:])
my_list[2:4] = [3, "dog"]
print(my_list[:])

cars = ["toyota","bmw"]
cars.append("VW")
print(cars)

cars.extend(["Jaguar","Audi"])
print(cars)

#cobmine two lists with +
print(my_list+cars)

#using insert
cars.insert(-1, "Subaru")
print(cars)

#deleting from lists

del cars[-1]
print(cars)

#deleting a list
del cars
print(cars) #gives name error

#pop method to remove items
print(cars.pop()) #removes and returns last item

cars.pop(1) #removes 1st item
print(cars)

#remove method (used by passing object to be removed)
cars.remove("VW")
print(cars)

#clear method. used for clearing list
cars.clear()

#copy method, count




