import requests
from bs4 import BeautifulSoup
import random

url ="https://en.wikipedia.org/wiki/Elon_Musk"
source = requests.get(url)
text = source.text
soup = BeautifulSoup(text,"lxml")
for link in soup.find_all("img",{"class":"thumbimage"}):
    href = str(link.get('src'))
    bingo = ('https:' + href)
    image_link = requests.get(bingo)
    img = str(random.randrange(1, 100))
    full_name = 'D:\python image\\' + str(img) + ".jpg"
    f = open(full_name,'wb')
    f.write(image_link.content)
    f.close()