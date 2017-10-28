# -*-coding:utf-8 -*-
"""
Dec:
Created on : 2017.10.28
Author: Iflier
"""
print(__doc__)

from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style, Back

url = "https://movie.douban.com/top250"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
}

init(autoreset=True)

i = 0
while True:
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'lxml')
    for div in soup.find_all('div', class_='hd'):
        i += 1
        print("{0:^5,d}\t{1}".format(i, div.find('span', class_='title').string))
    try:
        nextLink = soup.find('span', class_='next').a['href']
    except TypeError as err:
        print("{0}{1}{2}End.".format(Fore.CYAN, Back.BLUE, Style.BRIGHT))
        break
    url = urljoin(url, nextLink)
