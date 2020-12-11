#FIND BOOKS WITH 3 STARS RATING AT books.toscrape.com

import bs4
import requests

page_num = 1
base_url = f'http://books.toscrape.com/catalogue/page-{page_num}.html'

req = requests.get(base_url)

soup = bs4.BeautifulSoup(req.text, 'lxml')
books_at_page = soup.select('.product_pod')

for every_book in books_at_page:
    if len(every_book.select('.star-rating.Three')) > 0: #we need to fill out the spaces with dots .....
        print(every_book.select('a')[1]['title']) 

        #if its indeed 3 star rating then its not empty
        #so we r just grabbing element <a href> which is a link with a title text of a book and looking for title tag
        #and bcs of <a href> also has an image, so we want to grab a title not the image link so we use [1] not [0]

print(f'\nI found {len(books_at_page)} book(s) at page №{page_num}')

def decorate_book(func):
    def wrap_up():
        print(f'<=======PAGE {page_num}=======>')
        func()
        print(f'<====================>')

    return func

@decorate_book
def show_books_with_rating(rating_str):
    request = requests.get(base_url)

    parced_soup = bs4.BeautifulSoup(request.text, 'lxml')
    books_page = parced_soup.select('.product_pod')
    
    for every_book in books_page.select(f'.star-rating.{rating_str}'):
        print(f"Title: {every_book.select('a'[1]['title'])}")
        print(f"Price: {every_book.select('.price_color')['p'][0]}")


show_books_with_rating('Five')