import os
from urllib import urlopen
from bs4 import BeautifulSoup

data = urlopen("http://openapi.naver.com/search?key=0bed0a617ec4a99b3fb8029a10768085&query=%EC%A3%BC%EC%8B%9D&target=news&start=1&display=20").read()
soup = BeautifulSoup(data)

for item in soup.select('item'):
	title = item('title')[0].text.replace("!","").replace("\"","").replace(":","").replace("?","").replace("<b>","").replace("</b>","") +".html"
	if os.path.isdir("./07.18")==False:
		os.mkdir("./07.18")
	file = open("07.18/"+title,"w")
	url = item('link')[0].text
	data2 = urlopen(url).read()
	file.write(data2)