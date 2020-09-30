from bs4 import BeautifulSoup
import requests
url = "https://finance.yahoo.com/quote/TSLA/"
url2 = "https://finance.yahoo.com/quote/%5EGSPC/"
res = requests.get(url)
res2 = requests.get(url2)
soup = BeautifulSoup(res.text,"lxml")
soup2 = BeautifulSoup(res2.text,"lxml")
s=soup.find('div',{"class":"My(6px) Pos(r) smartphone_Mt(6px)"}).find("span").text
print("TSLA    :",s)
z=soup.find('div',{"class":"My(6px) Pos(r) smartphone_Mt(6px)"}).find_all("span")[1].text
print("Changes :",z)
n=soup2.find('div',{"class":"My(6px) Pos(r) smartphone_Mt(6px)"}).find("span").text
print("S&P 500 :",n)
m=soup2.find('div',{"class":"My(6px) Pos(r) smartphone_Mt(6px)"}).find_all("span")[1].text
print("Changes :",m)
print("TSLA :",url," S&P 500 :",url2)


