import requests

from bs4 import BeautifulSoup

import string


def get_content(url):
    r = requests.get(url)
    s = BeautifulSoup(r.content, 'html.parser')
    return s.find('p', class_="article__teaser").text


def format_title(title):
    title = title.strip()
    for _ in title:
        if _ in string.punctuation:
            title = title.replace(_, '')
    title = title.replace(' ', '_')
    return title


user_url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'
response = requests.get(user_url)
soap = BeautifulSoup(response.content, 'html.parser')
all_articles = soap.findAll('li', class_='app-article-list-row__item')
correct_articles = {}

for _ in all_articles:
    article_type = _.find('span', class_='c-meta__type').text
    if article_type == 'News':
        article_title = _.find('a', {'data-track-action': 'view article'})
        inner_link = 'https://www.nature.com' + article_title['href']
        content = get_content(inner_link)
        correct_articles.update({format_title(article_title.text): content})

for key, value in correct_articles.items():
    with open(f'{key}.txt', 'wb') as file:
        file.write(bytes(value, 'utf-8'))
