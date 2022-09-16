def greet():
    """
    This function used to greet user
    """
def greetwithargs(name):
    """with arguments"""
    print("Hello " + name)

greetwithargs("Oscaros")

#print documentation of function
print(greet.__doc__)

# with return statement
def add(no1, no2):
    return no1 + no2

print(add(1,99))

#empahasising datatypes
def greetUser(name: str) -> str:
    return f"Good evening {name}"

print(greetUser("Oscaros"))

#default argumets
def multiply(a, b=3):
    return a * b
print(multiply(2))

#keyword arguments
# def login(user, pass):
#     print(user, pass)
# login(user="admin", pass="abc123")

#abitrary functions- uknown no of args
def summation(*args):
    print(sum(args))
summation(1,2,3,4,5)