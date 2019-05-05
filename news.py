import requests #api
from bs4 import BeautifulSoup #parser html




def news():#recupère les news par API et créer une liste de liste avec les informations comme le titre, le corps, la source et la date
    response = requests.get('https://data.messari.io/api/v1/news').json()
    articles = list()
    for news in response['data']:
        title = BeautifulSoup(news['title'], "html.parser").get_text()
        content = BeautifulSoup(news['content'], "html.parser").get_text()
        source = news['references'][0]['url']
        date = BeautifulSoup(news['published_at'], "html.parser").get_text()
        articles.append([title, content, source, date])
    return (articles)
