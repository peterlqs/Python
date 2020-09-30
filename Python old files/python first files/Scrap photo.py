import requests
from bs4 import BeautifulSoup
import random
import urllib
url ="https://www.creativeshrimp.com/top-30-artworks-of-beeple.html"
source = requests.get(url)
text = source.text
soup = BeautifulSoup(text,"lxml")
for link in soup.find_all("a",{"class":"lightbox"}):
    href = link.get('href')
    print(href)
    print(type(href))
    img = random.randrange(1, 500)
    full_name = str(img) + ".jpg"
    urllib.request.urlretrieve(href, full_name)
    print("loop break")