from bs4 import BeautifulSoup
import requests
import sys

#Check if in
books = {}
count = 0
book_list={}
def count_books():
    #if book name isnt in list yet, count = 0
    print("count_book's def")
    for book_name in books:
        book_name = books[book_name]
        print("Through count book")
        print(book_name)
        if book_name not in book_list:
            book_list[book_name]=0
        #else if alr in list and appear on web then +1
        if book_name in book_list and book_name in soup:
            add = book_list[book_name] + 1
            book_list[book_name]=add
            print(book_list)

#getting web information
def information():
    global urls,soup
    for i in urls:
        print("information def")
        web_name =urls[i]
        print(web_name)
        res = requests.get(web_name)
        soup = str(BeautifulSoup(res.text, "lxml"))
        count_books()
    print(book_list," im from information")
    sys.exit()

#Books
def get_books():
    print("get book def")
    global books,lists
    books={}
    count=0
    while True:
        book_name = input("More book? If done press d!")
        if book_name == "d":
            get_url()
        else:
            count += 1
            books["a{}".format(count)] = book_name
            print(books)




#Web page
#url = input("Enter url")
def get_url():
    print("get url def")
    global urls
    urls = {}
    count = 0

    print("Press Ctrl+D to stop input.")
    userInput = sys.stdin.readlines()

    def removen():
        if "\n" in userInput:
            userInput.remove("\n")
            removen()
        else:
            pass
    removen()
    for iz in userInput:
        count += 1
        urls["w{}".format(count)] = iz
    print(urls)
    information()
#to run
get_books()
