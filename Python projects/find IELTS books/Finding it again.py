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
        print(book_name)
        if book_name not in book_list:
            book_list[book_name]=0
            print(book_list)
        if book_name in book_list:
            print("yes")
        #else if alr in list and appear on web then +1
        if book_name in book_list and book_name in soup:
            add = book_list[book_name] + 1
            book_list[book_name]=add
            print(book_list)




#getting web information
def information():
    global urls,soup
    for i in urls:
        web_name =urls[i]
        res = requests.get(web_name)
        soup = str(BeautifulSoup(res.text, "lxml"))
        count_books()
    print(book_list," im from information")
    sys.exit()

#Books
def get_books():
    global books,lists
    lists={}
    count=0

    print("Press Ctrl+D to stop input.Book side.")
    books = sys.stdin.readlines(2)

    def removen():
        if "\n" in books:
            books.remove("\n")
            removen()
        else:
            pass

    removen()
    for i in books:

        count += 1
        lists["a{}".format(count)] = i
    information()

#Web page
#url = input("Enter url")
def get_url():
    global urls
    urls = {}
    count = 0
    for i in range(1):
        print("Press Ctrl+D to stop input.")
        userInput = sys.stdin.readlines()

        def removen():
            if "\n" in userInput:
                userInput.remove("\n")
                removen()
            else:
                pass

        removen()
        for i in userInput:
            count += 1
            urls["w{}".format(count)] = i
    get_books()

get_url()
