import requests

from bs4 import BeautifulSoup

import string

import os

# import time

# from datetime import datetime


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

"""
def get_current_time():
    timestamp = time.time()
    date_time = datetime.fromtimestamp(timestamp)
    return date_time.strftime('%d-%m-%Y, %H-%M-%S')
"""

user_url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page='
user_pages_qty = int(input())
user_article_type = input()
# time_stamp = get_current_time()
for page_num in range(1, user_pages_qty + 1):
    response = requests.get(user_url + str(page_num))
    soap = BeautifulSoup(response.content, 'html.parser')
    all_articles = soap.findAll('li', class_='app-article-list-row__item')
    correct_articles = {}

    for _ in all_articles:
        article_type = _.find('span', class_='c-meta__type').text
        if article_type == user_article_type:
            article_title = _.find('a', {'data-track-action': 'view article'})
            inner_link = 'https://www.nature.com' + article_title['href']
            content = get_content(inner_link)
            correct_articles.update({format_title(article_title.text): content})

    os.makedirs(f'Page_{page_num}')
    for key, value in correct_articles.items():
        with open(f'Page_{page_num}//{key}.txt', 'wb') as file:
            file.write(bytes(value, 'utf-8'))
print('Saved all articles.')
