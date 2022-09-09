# Write a python program to fetch only Email ID from text file which include following fields -:
# Name
# Mobile Number
# Roll Number
# Email ID
textfile = 'assignments/week4/textfile.txt'
email = None

with open(textfile) as f:
    i = -1
    for line in f:
        if line.startswith('Email:'):
            email = line
print(email)
