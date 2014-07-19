import os
from urllib import urlopen
from bs4 import BeautifulSoup

os.mkdir('07.17')

data = urlopen('http://www.huffingtonpost.kr/the-news/2014/07/17').read()
soup = BeautifulSoup(data)

for item in soup.select('h3 a'):
	title = item.text.replace("!","").replace("\"","").replace(":","").replace("?","") +".txt"
	title = "07.17/" + title
	url = item.get('href')
	
	file = open(title,"w")
	data2 = urlopen(url).read()
	soup2 = BeautifulSoup(data2)
	
	for s in soup2.findAll('.content p'):
		file.write(s.text.encode('utf-8'))