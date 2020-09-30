import requests
import bs4
url = 'http://books.toscrape.com/catalogue/page-{}.html'
two_star_titles = []
count = 0
for n in range (1,51):
    res = requests.get(url.format(n))
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    products = soup.select(".product_pod")
    for book in products:
        if len(book.select('.star-rating.Two')) != 0 :
            count += 1
            book_title = book.select('a')[1]['title']+ "\n"
            two_star_titles.append(book_title)
print("".join(two_star_titles))
print(count)



