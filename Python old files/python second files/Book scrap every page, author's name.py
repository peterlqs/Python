import requests
import bs4
count = 1
url = "http://quotes.toscrape.com/page/{}/"
list =[]
yesh = True
while yesh:
    urlz = url.format(count)
    res = requests.get(urlz)
    soup = bs4.BeautifulSoup(res.text,"lxml")
    count += 1
    if "No quotes found!" in res.text:
        break
    for n in soup.select(".author"):
        new = n.text + "\n"
        if new not in list:
            list.append(new)
print("".join(sorted(list)))