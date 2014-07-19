import os
from urllib import urlopen
from bs4 import BeautifulSoup

os.mkdir('07.18')

data = urlopen('http://openapi.naver.com/search?key=0bed0a617ec4a99b3fb8029a10768085&query=%EC%A3%BC%EC%8B%9D&target=news&start=1&display=20').read()
soup = BeautifulSoup(data)

for item in soup.select('item originallink'):
        title = item.text.replace("!","").replace("\"","").replace(":","").replace("?","") +".txt"
        
        file = open(title,"w")
        url = item.get('link')        
        data2 = urlopen(url).read()
        soup2 = BeautifulSoup(data2)
        for s in soup2.findAll('.article_body'):
                file.write(s.text.encode('utf-8'))