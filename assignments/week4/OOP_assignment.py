'''
Using a class of your choice, implement ploymorphism, encapsulation, inheritance
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



