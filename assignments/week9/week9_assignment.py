'''
Find top movies on IMDB since 1980 using web scraping and save the result in a csv file. 
The csv file should have the following columns: title, year, rating, metascore, votes, 
gross, director, actors, runtime, genre, description. The csv file should be sorted by rating in descending order. 
The csv file should have the following columns: title, year, rating, metascore, votes, gross, director,
 actors, runtime, genre, description. The csv file should be sorted by rating in descending order.
'''
import csv
import requests
from bs4 import BeautifulSoup


def MovieByYear():
    text = ""
    text2 =""
    #loop through the years from 1980 to 2022..I onsidered last 10 years only to preserve file size
    for year in range(2022, 2022+1):
        req = requests.get(f"https://www.imdb.com/search/title/?release_date={year},&view=advanced").text.strip()
        text= text + req
        print(f"obtaining pagination Info for year {year}")

        parser = BeautifulSoup(text, "html.parser")
        page_end = parser.find(class_ = 'nav').find("div", class_="desc").find("span").text
        page_end = int("".join(page_end.split("of", 1)[1].split('titles.', 1)[:1]).replace(',' , ''))

        for nextpage in range(1, 100, 50): #you can replace 500 with page_end to fetch all records (very large file size)
            main_req = requests.get(f"https://www.imdb.com/search/title/?release_date={year},&start={nextpage}&view=advanced").text.strip()
            text2= text2 + main_req
            print(f"fetching pages {nextpage}-{nextpage+50} for year {year}")
    # return year, page_end


    # save text in html file for better perf
    with open('txt.html', 'w', encoding='utf-8') as file:
        file.write(text2)

    # read html file
    with open('txt.html', 'r', encoding='utf-8') as file:
        parser2 = BeautifulSoup(file, 'html.parser')
        higher_div = parser2.find_all(class_ = "lister-list")
        mid_div = parser2.find_all(class_="lister-item mode-advanced")
        movies=[]
        
        # loop through first div
        for index, t in enumerate(higher_div):
            # loop thru inner div
            for index, t in enumerate(mid_div):
                try:
                    # print(index)
                    # access individual elements
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
                    genre= t.find("div", class_="lister-item-content").find("p", class_="text-muted").find("span", class_="genre").string 
                    description= t.find("div", class_="lister-item-content").select("p:nth-child("+str(4)+")")
                    # print(type(genre))
                    

                    # create a dict on the fly
                    dic= {"title": title, 
                            "year": year_sanitized, 
                            "rating": rating, 
                            "metascore": metascore,
                            "votes":votes,
                            "director":director,
                            "actors":actors,
                            "runtime":runtime,
                            "genre":genre,
                            "description":description,
                    }

                    movies.append(dic)
                except AttributeError:
                    pass

                

        #exit()
        # print(type(movies))

        # write to csv
        with open('movies.csv', 'w') as csvfile:
            print("Writing csv")
            writer = csv.DictWriter(csvfile, fieldnames = ['title', 'year', 'rating', 'metascore', 'votes', 'director', 'actors', 'runtime', 'genre', 'description'], extrasaction = 'ignore')
            writer.writeheader()
            writer.writerows(movies)
            print("csv written")

#MovieByYear()

'''
Scrap Hacker News project and save the result in a csv file. 
The csv file should have the following columns: title, link, points, comments, author, rank. 
The csv file should be sorted by rank in ascending order.
https://news.ycombinator.com/

'''

url = "https://news.ycombinator.com/"
req = requests.get(url).text

bs = BeautifulSoup(req, "html.parser")
titleContainer = bs.find("table", class_="itemlist").find_all("tr", class_="athing")


for items in titleContainer:
    title = items.find_all("td", class_="title")[1].find("span", class_="titleline").find("a").text
    link = items.find_all("td", class_="title")[1].find("span", class_="titleline").find("a")["href"]
    points = items.find("table", class_="itemlist").find_all("td", class_="")

    comments
    x ="".join(comments.split())


    print(points)
# link = 
# points = 
# comments =
# author =
# rank =