'''
Find top movies on IMDB since 1980 using web scraping and save the result in a csv file. 
The csv file should have the following columns: title, year, rating, metascore, votes, 
gross, director, actors, runtime, genre, description. The csv file should be sorted by rating in descending order. 
The csv file should have the following columns: title, year, rating, metascore, votes, gross, director,
 actors, runtime, genre, description. The csv file should be sorted by rating in descending order.
'''
import csv
import re
import requests
from bs4 import BeautifulSoup
import os

text = ""
#loop through the years from 1980 to 2022
# for i in range(2022, 2022+1):
req = requests.get(f"https://www.imdb.com/search/title/?release_date=2022-01-01,&start=51&view=advanced").text
text= text + req


parser = BeautifulSoup(text, "html.parser")

higher_div = parser.find(class_ = "lister-list").find_all(class_="lister-item mode-advanced")

for t in higher_div:
    try:
        # print(t)
        title = t.find(class_="lister-item-content").find(class_ = "lister-item-header").find("a").text
        year = t.find(class_="lister-item-content").find(class_ = "lister-item-header").find("span", class_="lister-item-year text-muted unbold").text
        year_sanitized = ''.join(filter(lambda i: i.isdigit(), year))
        rating= t.find("div", class_="lister-item-content").find("div", class_="ratings-bar").find("div", class_="inline-block ratings-imdb-rating").find("strong").text
        metascore=t.find("div", class_="lister-item-content").find("div", class_="ratings-bar").find("div", class_="inline-block ratings-metascore").find("span").text
        votes = t.find("div", class_="lister-item-content").find("p", class_="sort-num_votes-visible").select_one("span[name*=nv]").text
        # gross=
        director=t.find("div", class_="lister-item-content").find("p", class_="").find("a").text
        actors=t.find("div", class_="lister-item-content").find("p", class_="").find_all("a")
        # for actor in actors:
        p=[actor.text for actor in actors]
        actors = p
        
        runtime= t.find("div", class_="lister-item-content").find("p", class_="text-muted").find("span", class_="runtime").text 
        genre= t.find("div", class_="lister-item-content").find("p", class_="text-muted").find("span", class_="genre").text 
        description= t.find("div", class_="lister-item-content").select("p:nth-child("+str(4)+")")
        # print(description)

        movies = [{"title": title, 
        "year": year_sanitized, 
        "rating": rating, 
        "metascore": metascore,
        "votes":votes,
        "director":director,
        "actors":actors,
        "runtime":runtime,
        "genre":genre,
        "description":description,
        }]

    except AttributeError:
        pass
    #exit()
# print(movies.values())

with open('movies.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = [])
    writer.writeheader()
    writer.writerows(movies)
    print("csv written")

'''
Scrap Hacker News project and save the result in a csv file. 
The csv file should have the following columns: title, link, points, comments, author, rank. 
The csv file should be sorted by rank in ascending order.
https://news.ycombinator.com/

'''