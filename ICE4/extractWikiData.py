import requests
from bs4 import BeautifulSoup
import os
x=requests.get("https://en.wikipedia.org/wiki/Music")
y=BeautifulSoup(x.content,"html.parser")
result=y.find_all('div')
for div in result:
    R1=div.find('h1')
    if R1!=None:
        print(R1.string)
result2=y.find_all('body')
for body in result2:
    result3=body.find_all('div')
    for div in result3:
        R2 = div.find('h1')
        if R2!= None:
            print(R2.string)
#r2=y.find('body')
#print(r2.get_text())


