# 10 questions about classes, objects, inheritance, polymorphism, queues, stacks, and more


'''
1. create a credit card class with the following attributes: card number, expiration date, and security code. 
Create a method that will print out the card number, expiration date, and security code. 
Create an instance of the class and call the method.'''

class creditCard:
    #attributes of the creditcard
    def __init__(self, card_number, exp_date, security_code):
        self.card_number = card_number
        self.exp_date = exp_date
        self.sec_code = security_code

    #method to display info
    def  displayInfo(self) -> str:
        print(f"Card Number is: {self.card_number} \nExpiration date is: {self.exp_date} \nSecurity code is: {self.sec_code}")

    
#Instantiate the class
creditCardInst = creditCard("04002888298", "2025-01-30", "245")
#call the display method
creditCardInst.displayInfo()



'''
2. create Animal class and Dog class. Make the Dog class inherit from the Animal class. Add a bark method to the Dog class. 
Create an instance of the Dog class and call the bark method.
'''
class animal:
    def __init__(self, name):
        self.animal_name = name
        #print(self.animal_name)
    
class dog(animal):
    def __init__(self, name):
        self.animal_name = name

    def bark(self):
        print(f"I bark Woof wwooof since im a {self.animal_name}")

#animalInst= animal()
dogClassinst = dog("dog")
dogClassinst.bark()



'''
3. create a class called Queue. The class should have the following methods: enqueue, dequeue, and size. 
The enqueue method should add an item to the queue. The dequeue method should remove an item from the queue. 
The size method should return the size of the queue.
'''
class Queue:
    
    def __init__(self) -> None:
        self.queue = list()
        self.max_size = 5

    def sizeOfqueue(self):        
        return len(self.queue)

    #check if queue is full
    def enqueue(self, data):
        if self.sizeOfqueue() > self.max_size:
            print(f"Queue is already full thus {data} wont be added to the Queue. Queue is currently {self.queue}")
        else:
            self.queue.append(data)
            print(f"{data} has been added to the Queue. Queue is currently {self.queue}")
    
    #check if queue is empty
    def dequeue(self):
        if not self.sizeOfqueue() < 1:
            print(f"{self.queue.pop(0)} has been removed from the Queue. Queue is currently {self.queue}")
        else: 
            print("Queue is already empty")

#instantiate class n objs
c = Queue()
c.enqueue(1)
c.enqueue(2)
c.enqueue(3)
c.enqueue(4)
c.enqueue(5)
c.enqueue(6)
#at this level since the maxsize set is 5, overflow occurs with error that queue is full, 7 & 8 wont be added

c.enqueue(7)
c.enqueue(8)

#remove some elements from the queue
c.dequeue()
c.dequeue()
c.dequeue()



'''
4. create a class called Stack. The class should have the following methods: push, pop, and size. 
The push method should add an item to the stack. The pop method should remove an item from the stack. 
The size method should return the size of the stack.
'''
class Stack:
    def __init__(self):
        self.stack = list()
        self.max_stack_size = 5
        
    def push(self, data):
        self.stack.append(data), print(f"{data} added to Stack. it currently contains {self.stack}") if self.size() < self.max_stack_size else print (f"{data} wont be added to Stack beacuse it is already full")
    def pop(self):
        print(f"{self.stack.pop()} removed from Stack. it currently contains {self.stack}") if self.size() > 1 else print ("Stack is already empty")
    def size(self):
        return len(self.stack)

s = Stack()
s.push('O')
s.push('S')
s.push('C')
s.push('A')

#these wont be added
s.push('R')
s.push('O')
s.push('S')

#pop elements
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()


'''
5. create a class called Person. The class should have the following attributes: name, age, and address. 
The class should have the following methods: eat, sleep, and work. The eat method should print out the name of the person and the word "is eating". 
The sleep method should print out the name of the person and the word "is sleeping". The work method should print out the name of the person and the word "is working".
'''
class person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def work(self):
        print(f"{self.name} is working")


p = person("Oscar Komuntu", 29, "Kirinya")
p.eat()
p.sleep()
p.work()


'''
6. create a class called Employee. The class should have the following attributes: name, age, and salary. 
The class should have the following methods: eat, sleep, and work. The eat method should print out the name of the person and the word "is eating". 
The sleep method should print out the name of the person and the word "is sleeping". 
The work method should print out the name of the person and the word "is working". 
Create a subclass of Employee called Programmer. 
The Programmer class should have the following attributes: name, age, salary, and programming language. 
The Programmer class should have the following methods: eat, sleep, work, and code. 
The code method should print out the name of the person and the word "is coding in" and the programming language. 
Create an instance of the Programmer class and call all the methods.
'''

class employee:
    def __init__(self, name, age, salary):
        self.name= name
        self.age = age
        self.salary = salary

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def work(self):
        print(f"{self.name} is working")

    
class programmer(employee):
    def __init__(self, name: str, age: int, salary: int, programming_language: str):
        self.name = name
        self.age=age
        self.salary = salary
        self.programming_lang = programming_language
        super().__init__(name, age, salary)
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def work(self):
        print(f"{self.name} is working")

    def code(self):
        print(f"{self.name} is coding in {self.programming_lang}")

prog = programmer("Oscaros Alvez", 29, 12000000, "python")
prog.eat()
prog.sleep()
prog.work()
prog.code()




'''
7. create a class called Vehicle. The class should have the following attributes: make, model, and year. 
The class should have the following methods: start, stop, and drive. 
The start method should print out the make, model, and year of the vehicle and the word "is starting". 
The stop method should print out the make, model, and year of the vehicle and the word "is stopping". 
The drive method should print out the make, model, and year of the vehicle and the word "is driving". 
Create a subclass of Vehicle called Car. The Car class should have the following attributes: make, model, year, and color. 
The Car class should have the following methods: start, stop, drive, and park. 
The park method should print out the make, model, year, and color of the car and the word "is parking". 
Create an instance of the Car class and call all the methods.
'''
class vehicle:
    def __init__(self, make: str, model: str, year: str):
        self.make = make
        self.model = model
        self.year = year
        self.color = None

    def start(self):
        print("{}, {}, of {} is starting".format(self.make, self.model, self.year))

    def stop(self):
        print("{}, {}, of {} is stopping".format(self.make, self.model, self.year))

    def drive(self):
        print("{}, {}, of {} is driving".format(self.make, self.model, self.year))

class car(vehicle):
    
    def __init__(self, make: str, model: str, year: str, color):
        super().__init__(make, model, year)
        self.color = color

    def start(self):
        print("Car {} of model {}, of {} and color {} is starting".format(self.make, self.model, self.year, self.color))

    def stop(self):
        print("Car {} of model {}, of {} and color {} is stopping".format(self.make, self.model, self.year, self.color))

    def drive(self):
        print("Car {} of model {}, of {} and color {} is driving".format(self.make, self.model, self.year, self.color))

    def park(self):
        print("Car {} of model {}, of {} and color {} is parked".format(self.make, self.model, self.year, self.color))

newcarInst = car("Mazda", "Demio", "2022","Blue")
newcarInst.start()
newcarInst.drive()
newcarInst.stop()
newcarInst.park()




'''
8. create a class called Animal. The class should have the following attributes: name, color, and age. 
The class should have the following methods: eat, sleep, and make_sound. 
The eat method should print out the name of the animal and the word "is eating". 
The sleep method should print out the name of the animal and the word "is sleeping". 
The make_sound method should print out the name of the animal and the word "is making a sound". 
Create a subclass of Animal called Dog. 
The Dog class should have the following attributes: name, color, age, and breed. 
The Dog class should have the following methods: eat, sleep, make_sound, and bark. 
The bark method should print out the name of the dog and the word "is barking". 
Create an instance of the Dog class and call all the methods.
'''

class animal:
    def __init__(self, name, color, age ):
        self.name =name
        self.color = color
        self.age = age

    def eat(self):
        print("{} is eating")

    def sleep(self):
        print("{} is sleeping")

    def makesound(self):
        print("{} is making a sound")

class dog(animal):
    def __init__(self, name, color, age, breed):
        super().__init__(name, color, age)
        self.breed = breed


    def eat(self):
        print("{} of breed {} is eating".format(self.name, self.breed))

    def sleep(self):
        print("{} of breed {} is sleeping".format(self.name, self.breed))

    def makesound(self):
        print("{} of breed {} is making a sound".format(self.name, self.breed))

    def bark(self):
        print("{} of breed {} is barking".format(self.name, self.breed))


c =dog("Benny", "Grey", 20, "German Shepherd")
c.eat()
c.sleep()
c.makesound()
c.bark()







'''
9. create a class of your choice. It should have at least 3 attributes and 3 methods where one of the methods is a static method. 
Implement polymorphism, encapsulation, and inheritance.
'''
class Car:
    def __init__(self): 
        pass
        
    def timetakenToCoverDistance(self):
        return 0

#inheritance
class Kia(Car):
    def __init__(self, name, topspeed, distance):
        super().__init__()   
        self.topspeed = topspeed
        self.distance = distance 
        self.name = name   
        self.__performanceOffset = 0.75   #encapsulation
    
    def timetakenToCoverDistance(self):
        return round((self.distance / self.topspeed ) * self.__performanceOffset, 1)

    def myName(self):
        return self.name

#inheritance
class Mazda(Car):
    def __init__(self, name, topspeed, distance):
        super().__init__()
        self.topspeed = topspeed
        self.distance = distance
        self.name = name
        self.__performanceOffset = 0.80  

    def timetakenToCoverDistance(self):
        return round((self.distance / self.topspeed) * self.__performanceOffset, 1)

    def myName(self):
        return self.name

#polymophism
def showtimetaken(acar): #t = d/s
    print("{} will take {} hours to cover {} Km if at top speed of {} Km/hr".format(acar.myName(),acar.timetakenToCoverDistance(), acar.distance, acar.topspeed))
    

# instantiate the objects
newKia = Kia("Kia", 180, 300)
newMazda = Mazda("Mazda", 220, 300)
showtimetaken(newKia)
showtimetaken(newMazda)



