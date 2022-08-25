#Qn1. program to sum up all items in a list. List shd be generated using list comprehension. size shd be from userinput

user_input = int(input("Enter the size of the list \n"))
my_list = [ x for x in range(user_input)]
print(my_list) 

x = 0
for i in range(user_input):
   x = x + my_list[i] 
print(x)



#qn2. count no of strings where string length is 2 or more and 1st and last character are same from a given list of strings
my_other_list = ['abc','xyz','aba','1221']
count = 0
for t in my_other_list:
    if len(t) >= 2:  
        if t[0] == t[-1]:           
                count += 1
                print ("String " +str(t)+ " is of " +str(count)+ " characters" )

#Qn3 program to remove duplicates from a list
fruits = ["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]
new_list = []

for c in fruits: #scan thru fruits
    if c not in new_list:#check for items which do not already exist atleast once in new list
        new_list.append(c)

fruits = new_list
print (new_list)

#Qn4 Program to print a specified list after removing 0th ..4th and 5th elements
sample_list = ['Red','Green','White','Black','Pink', 'Yellow']
index_list = [0,4,5]
new_list = []

for x in sample_list: #loop thru main list
    if sample_list.index(x) not in index_list: #get index of each item and compare aginst unwanted indices list, if no match - append to new list
        new_list.append(x)
print(new_list)

#qtn5: Program to generate a list except for the 1st 5 elements, where the values are squares of no.s between 1 and 30 both included
my_listo = [2 ** x for x in range(30)] #use list comprehension to print squares of 1st 30 sqrs
print(my_listo[5:])# display list without the 1st 5 elements

