import os
os.mkdir("Alex")
os.makedirs("Alex/hi")
os.rename("Alex","Daye")
os.rmdir("Alex")
os.path.abspath"""절대경로"""(path"""상대경로""")

#폴더 경로를 합치는 것
os.path.join

#실제로 존재하는 놈인지 확인
os.path.exists(path)

from urllib import urlopen
from bs4 import BeautifulSoup

data = urlopen('http://www.huffingtonposter.kr/').read()
soup = BeautifulSoup(data)
print soup.select('h1 a')[0].text

for font_name in soup.findAll('img'):
	print'