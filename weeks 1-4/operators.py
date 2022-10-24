# +, -, *. /, //, %, **, <, >, ==, =<, =>, <>
a =10
b =5

# print(f"a * b = {a * b}")
# print(f"a | b = {a / b}")
# print(f"a || b = {a // b}")
# print(f"a % b = {a % b}")
# print(f"a ** b = {a ** b}")
print(f"a < b = {a < b}")

# print("a > b {}".format(a > b))

# c=7 
# c |= 5  
# print(c)


#voting e.g
voting_age = 18
my_age = int(input("input ur age \n"))
is_reg = int(input("input 1 if reg 0r 0 if not \n"))

if my_age >= 18 and is_reg == 1:
    print("you are allowed to vote")
else:
    print("you are not allowed to vote")
