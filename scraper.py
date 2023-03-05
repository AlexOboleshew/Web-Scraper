import requests


def request_get_quotes(url):
    response = requests.get(url)
    if response.status_code == 200 and 'content' in response.json():
        print(response.json()['content'])
    else:
        print("Invalid quote resource!")


user_url = str(input())
request_get_quotes(user_url)
