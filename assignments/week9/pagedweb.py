import requests
from bs4 import BeautifulSoup
import json, re

my_input = input("What pdt do you want to search for")

myurl = f"https://www.newegg.ca/p/pl?={my_input}"

req = requests.get(myurl).text
breakpoint()
sup = BeautifulSoup(req, 'html.parser')
print(sup)