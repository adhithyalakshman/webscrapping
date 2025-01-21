from bs4 import BeautifulSoup
import requests
urlm="https://www.imdb.com/list/ls099876335/"
respon=requests.get(url=urlm)
content=respon.text
print(content)
soup=BeautifulSoup(content,'lxml')
print(soup.title.string)
mn=soup.findAll(name='div')
print(mn)
