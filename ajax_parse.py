
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
from selenium import webdriver

def get_lpage(url):
    driver = webdriver.PhantomJS()
    driver.get(url)
    last=driver.find_element_by_id(id_='paging').text.split(' ')[-1]
    return last


def to_csv(data):
    with open('/home/vsvld/projects/Parser/websites.csv', 'a') as file:
        order = ['name','link','traffic','type']
        # writer=csv.writer(file)
        writer=csv.DictWriter(file, fieldnames=order)
        writer.writerow(data)

def get_data(url):
    r=requests.get(url).text
    resp=r.strip().split('\n')

    for row in resp[1:]:
        row=row.split('\t')
        link=row[1]
        name=row[2]
        traffic=row[3]
        type=row[5]

        data={'name':name,
              'link':link,
              'traffic':traffic,
              'type':type}

        to_csv(data)

def main():

    url='https://www.liveinternet.ru/rating/'
    lpage=get_lpage(url)
    pages=list(range(1,int(lpage)+1))
    for page in pages:
        get_data(f'https://www.liveinternet.ru/rating///today.tsv?page={page}')



if __name__ == '__main__':
    main()
