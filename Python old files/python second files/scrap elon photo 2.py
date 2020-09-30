import requests
from bs4 import BeautifulSoup
import random
import urllib.request
url ="https://en.wikipedia.org/wiki/Elon_Musk"
source = requests.get(url)
text = source.text
soup = BeautifulSoup(text,"lxml")
for link in soup.find_all("img",{"class":"thumbimage"}):
    h = str(link.get('src'))
    bingo = ('https:' + h)
    image_link = requests.get(bingo)
    img = random.randrange(1, 100)
    full_name = 'D:\python image\\' + str(img) + ".jpg"
    urllib.request.urlretrieve(bingo, full_name)