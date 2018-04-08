'''
Adam Fidler
DIGHT 360
Assignment 4
'''

from bs4 import BeautifulSoup
import time
import re
import requests

url = 'https://reynoldsnlp.com/scrape/'
my_header = {'user-agent': 'Adam Fidler (fidlerja@byu.edu)'}
response = requests.get(url, headers=my_header)


def get_home():
    with open('./scrape/scrape.html', 'w+') as html_doc:
        html_doc.write(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        href_list = soup.find_all(href=re.compile(r'.html'))
    return href_list


def get_rnlp(filename):
    response = requests.get(url + filename, headers=my_header)
    with open('./scrape/' + filename, 'w+') as html_doc:
        html_doc.write(response.text)
    time.sleep(1.5)


def get_hrefs(filename):
    with open('./scrape/' + filename, 'r') as html_doc:
        soup = BeautifulSoup(html_doc, 'html.parser')
        hrefs = soup.find_all(href=re.compile(r'.html'))
        for href in hrefs:
            if href.get('href') not in final_list:
                final_list.append(href.get('href'))
    return final_list.sort()

master_hrefs = get_home()
master_names = []
final_list = []

for href in master_hrefs:
    master_names.append(href.get('href'))
    get_rnlp(href.get('href'))

for name in master_names:
    if name not in final_list:
        get_hrefs(name)

print('Done!\n')
if(input('Would you like to see the full list? (y/n) -') == 'y'):
    for item in final_list:
        print(item)
    print('='*38)
    print('hrefs gathered: ', end='')
    print(str(len(final_list)) + '/' + str(len(master_hrefs)))
    print('NOTE: fa.html is missing from the list.')
else:
    print('Good-bye!')

