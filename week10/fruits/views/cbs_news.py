import json
from flask import Blueprint, request, redirect, render_template
from bs4 import BeautifulSoup
import requests
from fruits.models import CBSNews

cbsviews = Blueprint('cbsviews', __name__)

def getCBSNEWS():
    url = "https://www.cbsnews.com/latest/rss/main"
    xml_data = requests.get(url).content 
    soup = BeautifulSoup(xml_data, 'xml')

    data = []

    for news in soup.find_all('item'):
        dataItem = { 
            'title': news.title.string,
            'link': news.link.string,
            'image': news.image.string,
            'description': news.description.string,
        }   
        data.append(dataItem)

    return data

@cbsviews.route('/cbs-news', methods=['GET', 'POST'])
def cbs_news():
    if request.method == 'POST':
        return redirect('/')

    #data from xml
    data = getCBSNEWS()

    # existing data from database
    cbsnews = CBSNews.get_all_news()

    # avoid duplication-replace all that doesnt exist in db
    for news in data:        
        if news.get('title').lower() not in [i.title.lower() for i in cbsnews]:
            hnew = CBSNews(title=news['title'], link=news['link'], image=news['image'], description=['description'])
            hnew.save()
        else:
            continue

    return render_template('cbs_news.html', data=cbsnews)

@cbsviews.route('/cbs-news/find', methods=['GET', 'POST'])
def search_cbs_news():
    query = request.args.get('q')
    # search the database 
    data = CBSNews.query.filter(CBSNews.title.like(f'%{query}%')).all()
    return {'data': [news.serialize() for news in data]}
