from re import sub


def add(**kwargs):
    print(sum(kwargs.values()))
    print(kwargs.get('a') - kwargs.get('b'))
add(a=1, b=3)


#lamda to add two numbers
addme = lambda y, x : y + x
print(addme(2,1))

# list1=[1,-2,3]
       

# def fun(a):

#     if(a>50):

#         return a-3

#     return fun(fun(a+5))


class Person:

    def __init__(self, name, age):

        self.name = name

        self.age = age

        age = 50

 

p1 = Person('Sam', 24)

print(p1.name, p1.age)