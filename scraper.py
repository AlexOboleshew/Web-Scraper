import requests

user_url = str(input('Input the URL:\n'))
response = requests.get(user_url)
if response:
    with open('source.html', 'wb') as source_code:
        page_content = response.content
        source_code.write(page_content)
        print('Content saved.')
else:
    print(f'The URL returned {response.status_code}')
