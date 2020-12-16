#IMPORT any libraries you think youll need to scrape a site
import bs4
import requests

#get the HTML text from quotes.toscrape.com (homepage)
answer = requests.get('http://quotes.toscrape.com/')

soup_html = bs4.BeautifulSoup(answer.text, 'lxml')

#get the names of all the authors at the first page
authors = set()

for quote in soup_html.select('.quote'):
    for author in quote.select('.author'):
        authors.add(author.getText())

authors = list(authors)
print(f'Authors from 1st page: {authors}')

#get the top 10 tags
top_10_tags = []

for tag_item in soup_html.select('.tag-item'):
    for tag in tag_item.select('.tag'):
        top_10_tags.append(tag.getText())

print(f'\nTop 10 tags: {top_10_tags}')

#get the names of all the authors FROM THE WHOLE SITE
all_authors = []

page_index = 1
page = 'http://quotes.toscrape.com/page/{page_index}/'

req = requests.get(page)
soup = bs4.BeautifulSoup(req.text, 'lxml')

while len(soup.select('.quote')) > 0:
    for quote in soup_html.select('.quote'):
        for author in quote.select('.author'):
            all_authors.append(author.getText())

    page_index += 1

print(f'\n All authors: {all_authors}')