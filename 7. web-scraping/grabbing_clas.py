import requests
import bs4
import lxml

result = requests.get("https://www.ispring.ru/")

text_from_result = bs4.BeautifulSoup(result.text, 'lxml')

print(text_from_result) #whole text

print("""
======================================================
NOW PARSING ONLY .text (. means class attribute)......

BELOW WHAT WE FOUND:

""")
print(text_from_result.select('.text')) #only class that contains text in the name (returns a list)

for text in text_from_result.select('.text'):
    print(text.getText())