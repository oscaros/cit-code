# END OF WEEK 7 QUIZ
'''
1. Your task is to create slightly different animals, which should have the same properties and methods, 
but should implement the talk() method in different ways. 
For example. should a cat (when talking) say "Moew", a dog "Woff", a fish "Blub" and a Cow "Muuu". 
They should all share the following (private) properties: name (string), age (number), food (list of strings), 
and have the functions get_name, set_name, get_age, set_age, get_food, add_food, remove_food. Finally, 
all the animals must have the talk function, but that function must, as I said, be implemented in each animal,
 as the animals have different sounds.
When you have made the classes, create instances of the classes and put in a list 
- loop through the list - and let all the animals talk! :)
'''
class Animal:
    def __init__(self, name:str, age: int, food: list):
        self.__name = name
        self.__food=list(food)
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age
        return self.__age

    def get_food(self):
        return self.__food

    def add_food(self, food):
        return self.__food.append(food)

    def remove_food(self, food):
        for x in self.__food:
            if x == food:
                self.__food.remove(food)
        return self.__food

    def talk(self):
        return 0

class Dog(Animal):
    def __init__(self, name:str, age: str, food: list, sound: str):
        
        super().__init__(name,age,food)
        self.__sound = sound

   
    def talk(self):
        return f"I {self.__sound}"

class Cat(Animal):
    def __init__(self, name:str, age: str, food: str, sound: str):
       
        super().__init__(name,age,food)
        self.__sound = sound


    def talk(self):
        return f"I {self.__sound}"

#Dog class
newDog = Dog("Crypto", 10, "Bones", "bark")
newDog.add_food("Bones")
newDog.set_age(10)
newDog.set_name("Crypto")
print(newDog.talk())

#cat class
newCat = Cat("Kitty", 10, "Bones", "Moeww")
newCat.add_food("Milk")
newCat.set_age(10)
newCat.set_name("Kitty")
print(newCat.talk())



'''
2. The snail climbs up 7 feet each day and slips back 2 feet each night. 
How many days will it take the snail to get out of a well with the given depth?. Using python, write a function to solve this problem.
Sample Input: 31
Sample Output: 6
'''
def NoOfDaysForSnail(depth):
    initial_feet = 7
    unscussfull_feet = 2
    final_successful_feet = initial_feet - unscussfull_feet

    no_of_days = depth // final_successful_feet
    print(no_of_days)

NoOfDaysForSnail(31)


'''
3. Write a function that takes a list of numbers and returns the largest number in the list.
'''
def LargestNo():
    #first sort the list
    MyList = [7,5,10,8,3]

    #sort in asc order using bubble sort
    i = 0
    while i<len(MyList):
        j = 0
        while j<len(MyList)-1:
            if MyList[j+1] < MyList[j]:
                MyList[j], MyList[j+1] = MyList[j+1], MyList[j]
            j += 1
        i += 1

    print("Largest number in {} is : {}".format(MyList, MyList[-1]))

LargestNo()




'''
4. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
`Hello world!`
Then, the output should be:
`UPPER CASE 1`
`LOWER CASE 9`
'''

def counter(word: str):
    upper = 0
    lower = 0

    for i in word:
        if i.isupper():
            upper += 1 
        else:
            lower += 1
    print("UPPER CASE is {} \nLOWER CASE is {}". format(upper, lower))
    
counter("Hello World")



'''
5. Using Object Oriented Programming, write a program that implements
a dice game. The game should have two players, and each player
should have a name and a score. The game should have a method
called `play` that takes two players as arguments and simulates
the game. The game should be played as follows:
    - Each player rolls a die.
    - The player with the highest roll wins the round.
    - The winner gets one point added to their score.
    - The game ends when one player has 5 points.
    - The player with the most points at the end of the game wins.
    - The program should print out the winner's name and score.
    - If a player rolls a 6, they get an extra roll. If they roll a 6 again, they get another extra roll. If they roll a 6 a third time, they get an extra roll, but their turn ends.
'''

class DiceGame:
    def __init__(self, players: list):
        self.players = players
        
    def play(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

class Player1:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class Player2:
    def __init__(self, name, score):
        self.name = name
        self.score = score






'''
6. Write a Python program that lists out all the default as well as custom properties of the class.
'''
print("6. Write a Python program that lists out all the default as well as custom properties of the class.")
class Animal2:
    def __init__(self, name: str, sound: str): 
        self.name = name
        self.sound = sound

AnimalInst = Animal2("Dog", "Barks")
print(dir(AnimalInst))

    



'''
7. Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, 
and traversal methods.
'''
class MyStack:
    def __init__(self, data: list):
        self.data = data

    def push(self, item):
        return self.data.append(item)

    def pop(self):        
        if not self.size() < 1:
            self.data.pop()
        else:
            print("Stack underflow")
        return self.data

    def traversal(self):
        for i in self.data:
            print(i)

    def size(self):
        return len(self.data)
    
newStack = MyStack([])
newStack.push(1)
newStack.push(2)
newStack.push(3)
newStack.push(4)
newStack.pop()
newStack.pop()
# newStack.pop()
# newStack.pop()
# newStack.pop()
newStack.traversal()
    




'''
8. Using list comprehension, write a program that takes a list of numbers and returns a list of the squares of the numbers.
'''
print([i**2 for i in range(1,10)])

'''
9. Using only functions and lists, Implement a queue data structure. The queue should have the following methods: enqueue, dequeue, and size. 
The queue should be "first-in-first-out" (FIFO).
'''
def sizeOfqueue(queue):        
    return len(queue)

#check if queue is full
def enqueue(data, queue, max_size):
    if sizeOfqueue(queue) > max_size:
        print(f"Queue is already full thus {data} wont be added to the Queue. Queue is currently {queue}")
    else:
        queue.append(data)
        print(f"{data} has been added to the Queue. Queue is currently {queue}")

#check if queue is empty
def dequeue(queue):
    if not sizeOfqueue(queue) < 1:
        print(f"{queue.pop(0)} has been removed from the Queue. Queue is currently {queue}")
    else: 
        print("Queue is already empty")

def main():
    max_size = 5
    queue = list()
    enqueue(1, queue, max_size)
    enqueue(2, queue, max_size)
    enqueue(11, queue, max_size)
    enqueue(10, queue, max_size)
    enqueue(8, queue, max_size)

    #at this level since the maxsize set is 5, overflow occurs with error that queue is full, 90 & 100 wont be added

    enqueue(90, queue, max_size)
    enqueue(100, queue, max_size)

    #remove some elements from the queue
    dequeue(queue)
    dequeue(queue)

if __name__ == "__main__":
    main()



'''
10. Using a while loop, implement merge sort algorithm.
'''
