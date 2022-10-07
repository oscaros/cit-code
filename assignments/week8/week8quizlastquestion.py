import os
import sys

# def CreateFile():
try:
    with open(os.getcwd()+'answers.txt', 'w') as file:
        file.write('Create a new text file!')
except FileNotFoundError:
    print("The 'docs' directory does not exist")