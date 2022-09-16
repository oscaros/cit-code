# #1 Create a 2-D array and slice out the second number in the second column
My2DArray = [["o", "s", "c"], ["a", "r", "o"]]
print(My2DArray[1:0][1])


# #2 Write a python program to sort array element in the ascending/descending order
# My2DArrayToSort = [1,4,6,7,9]
# My2DArrayToSort.sort()
# print("Acsending: {}".format(My2DArrayToSort))
# My2DArrayToSort.sort(reverse=True)
# print("Descending: {}".format(My2DArrayToSort))


# #3 Write a python program to find the maximum and minimum value in a given 2-D array
# MaxMin2DArray = [[1,3,5], [4,8,12]]
# MaxMin2DArrayMin = min(MaxMin2DArray)# get minimum value of 2-d array 1st
# MaxMin2DArrayMinlowest = min(MaxMin2DArrayMin)# get min o
# print("Minimum value of {} is: {}".format(MaxMin2DArray,MaxMin2DArrayMinlowest))

# MaxMin2DArrayMax = max(MaxMin2DArray)# get minimum value of 2-d array 1st
# MaxMin2DArrayMinhighest = max(MaxMin2DArrayMax)# get min o
# print("Maximum value of {} is: {}".format(MaxMin2DArray, MaxMin2DArrayMinhighest))

# #4 Write a python program to input 5 subject marks and calculate total marks, percentage and grade based on following criteria
# # percentage less than 50 (Grade C)
# # percentage equal to 50 and less than 80 (Grade B)
# # percentage equal to 80 and more than 80 (Grade A)


# def total(marks):    
#     return sum(marks)

# def avg(marks):
#     length = len(marks)
#     avg = total(marks)/length
#     #print(avg)
#     return avg

# def grade(marks):
#     grade=None
#     average = avg(marks)
#     if average < 50:
#         grade = "C"
#     elif average <= 50 and average < 80:
#         grade = "B"
#     elif average <= 80 and average > 80:
#         grade = "A"
#     else:
#         print("Uknown grade")

#     return grade

# def main():
#     inputMarks = input("Enter 5 subject marks separated by commas: ")
#     marks = []
#     marks = inputMarks.split(',')
#     marks =  list(map(int, marks))
#     #print(type(marks))
#     print(total(marks))
#     print(grade(marks))

# if __name__ == '__main__':
#     main()


# #5 Write a python program to fetch only Email ID from text file which include following fields -:
# # Name
# # Mobile Number
# # Roll Number
# # Email ID

# textfile = 'assignments/week4/textfile.txt'
# email = None

# with open(textfile) as f:
#     for line in f:
#         if line.startswith('Email:'):
#             email = line
# print(email)




#6 Write a function for checking the speed of drivers. This function should have one parameter: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total 
# number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended”

# def speedcheck(speed, points):    
#     speedLimit = 70    
#     if speed < 70:
#         print("Ok")
#     elif speed > 70:
#         computation(speed, speedLimit, points)

# def computation(inputSpeed,speedLimit,points):
#     difference = inputSpeed - speedLimit
#     pts = difference % 5
#     times = int((difference - pts) / 5); #this will give us the number of times 
#     points = times

#     if points < 12:
#         print("You have {} demerit points".format(points))
#     else:
#         print("Your license has been suspended")

# def main():
#     points = 0
#     inputSpeed= int(input("Enter speed: "))
#     speedcheck(inputSpeed,points )

# if __name__ == '__main__':
#     main()


#7 Write a function called show_stars(rows). If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****
# def show_stars(rows):
#     if rows == 5:
#         for i in range(rows+1):
#             print('*'*i)

# show_stars(5)


#8 Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 
# 5 between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
# numbers=[]
# for i in range(2000, 3200):
#     if (i%7==0) and (i%5!=0):
#         numbers.append(str(i))
# print (','.join(numbers))


#9 Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# numbers = input("Input a sequence of comma-separated numbers from console : ")
# list = numbers.split(",")
# #convert already generated list to tuple
# tuple = tuple(list)
# print('A list of {} is : {}'.format(numbers, list))
# print('A tuple of {} is : {}'.format(numbers, tuple))



#10 Write a program that calculates and prints the value according to the given formula:
#  Q = Square root of [(2 * C * D)/H] 
# Following are the fixed values of C and H: C is 50. H is 30. 
# D is the variable whose values should be input to your program in a comma-separated sequence. 
# Example Let us assume the following comma separated input sequence is given to the 
# program: 100,150,180 The output of the program should be: 18,22,24

# import math #import math lib to access sqr root funcs

# value_of_D = input("input comma separated list of items as value of D: ")
# value_of_D = value_of_D.split(',') # split D into a list
# C = 50
# H =30
# output = []

# for i in value_of_D:
#     calculate = round(math.sqrt(2 * C * int(i) / H))
#     output.append(calculate)

# print(output)


#11 Write a function to compute 5/0 and use try/except to catch the exceptions.
# def divide(x,y):
#     try:
#         divide = x/y
#         return divide
#     except ZeroDivisionError:
#         return "bad calculation"

# print(divide(5,0))


#12 Create a nesting list that prints out the color and the car brand.



#13 Bonus Question: Algorithm challenge: Create your own sorting algorithm.