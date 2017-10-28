# -*-coding: utf-8 -*-
"""
Dec: 获取页面http://news.baidu.com/的部分板块的新闻
Created on : 2017.10.27
Author: Iflier
"""
print(__doc__)

import requests
from bs4 import BeautifulSoup
from colorama import init, Style, Fore, Back


baseUrl = "http://news.baidu.com/"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
}


def formatContent(contentSoup, className):
    i = 0
    for liList in contentSoup.find_all("ul", class_=className):
        for news in liList.find_all('li', limit=10):
            i += 1
            print("{0:^7,d}\t{1}".format(i, news.find('a').contents[0]))

init(autoreset=True)
respMil = requests.get(baseUrl + "mil", headers=headers)
soupMil = BeautifulSoup(respMil.text, 'lxml')
print("{0}{1}{2}\t军事新闻：\t".format(Fore.GREEN, Back.RED, Style.BRIGHT))
formatContent(soupMil, "ulist")

respSociety = requests.get(baseUrl + 'society', headers=headers)
soupSociety = BeautifulSoup(respSociety.text, 'lxml')
print("\n{0}{1}{2}\t社会百态：\t".format(Fore.CYAN, Back.BLUE, Style.BRIGHT))
formatContent(soupSociety, "ulist")

respFinance = requests.get(baseUrl + 'finance', headers=headers)
soupFinance = BeautifulSoup(respFinance.text, 'lxml')
print("\n{0}{1}{2}\t财经新闻\t".format(Fore.CYAN, Back.BLACK, Style.BRIGHT))
formatContent(soupFinance, "ulist fb-list")
