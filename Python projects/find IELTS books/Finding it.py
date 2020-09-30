from bs4 import BeautifulSoup
import requests

#Books
b1 ="The Official Cambridge Guide to IELTS"
b2 ="Barron’s IELTS Superpack"
b3 ="Cambridge IELTS 13 Academic Student’s Book with Answers"
b4 ="Official IELTS Practice Materials"
b5 ="Road to IELTS"

#Count
c1=c2=c3=c4=c5=0

#Web page
#url = input("Enter url")
urlz = "https://ieltsliz.com/recommended-books-for-ielts/"
res = requests.get(urlz)
soup = str(BeautifulSoup(res.text,"lxml"))

#Check if in
if b1 in soup:
    c1+=1
if b2 in soup:
    c2+=1
if b3 in soup:
    c3+=1
if b4 in soup:
    c4+=1
if b5 in soup:
    c5 += 1

print(c1,c2,c3,c4,c5)





