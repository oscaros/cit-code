#program to count no.s to the nth term
n =int(input("enter nth term"))

sum = 0
counter =1

while counter <= n:
    sum = sum + counter
    counter = counter +1
print("The sum is ", sum)
