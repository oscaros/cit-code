#Loops assignment by Oscar Komuntu
#0783765634



#Qn 1 1st ten natural no.s
n = 0
while n < 10:
    n = n + 1
    print(n)

#Qn2 sum of all natural numbers from 1 to a given number
counter = 1;
sum = 0

inp = int(input("enter nth natural number \n"))

while counter <= inp:
    sum = sum + counter
    counter = counter + 1
print("sum is ", sum)

#Qn 3 multiplication table of a given number
num = int(input("enter no. to get multiplication table\n"))

for ex in range(1, num-1):
   print(num, 'by', ex, '=', num*ex)


#Qn4 print particlular no.s
magic = [12,75,150,180,145,525, 50]

for m in magic:
    if m % 5 == 0:
        print(m)
    elif m > 150:
        continue
    elif m > 500:
        break

#Qn5 total number of digits
n = 4673453
counter = 0
while n > 0:
    n //= 10 #use this to keep slicing off the last bit of the number
    counter += 1
print("No. of digits is ", counter)

#Qn6 display numbers from -10 to -1

counter = -10
while counter < 0:
    print(counter)
    counter = counter + 1
  


