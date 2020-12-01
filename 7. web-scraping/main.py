import requests
import bs4


result = requests.get('http://example.net/')
result_text = bs4.BeautifulSoup(result.text, 'lxml')

print(result_text.select('title')[0].getText()) #we using [index] to .getText() instead of HTML tag words
print(result_text.select('p')) #we also can see just every item in array

print(result_text.select('.icon'))

