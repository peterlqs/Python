from bs4 import BeautifulSoup
import requests
import sys
# Instruction:
print("Paste your books and links list then press Ctrl+D. Best way : Ctr+V --> Ctr+D Then wait...")
#Get book and url
count1=count2=1
url_list = {}
book_list = {}
new ={}
book_and_url = sys.stdin.readlines()
for i in book_and_url:
    book_and_url = [s.replace("\n","") for s in book_and_url]
    while "" in book_and_url:
        book_and_url.remove("")
for wordss in book_and_url:
    if "https://" in wordss:
        url_list["u{}".format(count1)] = wordss
        count1 += 1
    else:
        book_list["b{}".format(count2)] = wordss
        count2 += 1
#Scan if book is in url
for web in url_list:
    res = requests.get(url_list[web])
    soup = BeautifulSoup(res.text,"lxml")
    for bok in book_list:
        book = book_list[bok]
        if book not in new:
            new[book] = 0
        # else if alr in list and appear on web then +1
        if book in new and book in str(soup):
            add = new[book] + 1
            new[book] = add
#Print result
finish = sorted(new.items(),key=lambda x : x[1],reverse=True)
for i in finish:
    print(i[0]," : ",i[1])
