import requests

url = 'https://www.wikipedia.org'
my_header = {'user-agent': 'Adam Fidler (fidlerja@byu.edu)'}
response = requests.get(url, headers=my_header)
response.encoding = 'utf-8'
with open('wiki.html', 'w') as my_file:
    print(response.text, file=my_file)
i
