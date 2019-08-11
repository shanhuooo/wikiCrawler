#!/usr/bin/python3
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://wikipedia.hk.wjbk.site/wiki/Apple")
bsObj = BeautifulSoup(html)
for link in bsObj.findAll("a"):
	if 'href' in link.attrs:
		print(link.attrs['href'])