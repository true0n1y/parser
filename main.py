
import sys
sys.path =['', '/home/vsvld/anaconda3/lib/python37.zip',
'/home/vsvld/anaconda3/lib/python3.7',
'/home/vsvld/anaconda3/lib/python3.7/lib-dynload',
'/home/vsvld/anaconda3/lib/python3.7/site-packages',
'/home/vsvld/projects/Parser',
'/usr/lib/python37.zip',
'/usr/lib/python3.7',
'/usr/lib/python3.7/lib-dynload',
'/usr/local/lib/python3.7/dist-packages',
'/usr/lib/python3/dist-packages']

import requests
import time
import pandas as pd
import csv
from bs4 import BeautifulSoup



def get_html(url):
    r = requests.get(url)
    return r.text

def get_number(ratio):
    return ratio.split()[0].replace(',','')

def to_csv(data):
    with open('/home/vsvld/projects/Parser/plugins.csv', 'a') as file:
        writer=csv.writer(file)
        writer.writerow(data)




def get_data(html):

    soup = BeautifulSoup(html, 'lxml')
    deep_url = soup.find_all('section')[1].find('a')['href']
    deep_soup = BeautifulSoup(get_html(deep_url), 'lxml')
    targets = deep_soup.find_all('article', class_='plugin-card')
    rowsBox=[]

    for article in targets:
        pluggName=article.find('h2', class_='entry-title').find('a').text
        ratio=get_number(article.find('span', class_='rating-count').find('a').text)
        description=article.find('div', class_='entry-excerpt').find('p').text
        rowsBox.append([pluggName,ratio,description])


    for row in rowsBox:
        to_csv(row)
        # print(row)

def main():


    url = "https://wordpress.org/plugins/"
    #url = "https://wordpress.org"
    get_data(get_html(url))


if __name__ == '__main__':
    main()
