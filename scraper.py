import requests

import re

from bs4 import BeautifulSoup


def requests_get_summary(url):
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup = BeautifulSoup(response.content, features='html.parser')
    title = soup.find('title').text
    summary = soup.find('meta', {'name': 'description'})['content']
    result = {'title': title, 'description': summary}
    return result


def page_valid(url):
    return re.search('articles|nature.com', url)


user_url = str(input('Input the URL:\n'))
if page_valid(user_url):
    print(requests_get_summary(user_url))
else:
    print('Invalid page!')
