#web scraping
from urllib import request

url="http://www.naver.com"
content=request.urlopen(url)
print(content.read())