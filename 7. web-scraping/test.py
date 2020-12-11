import requests
import bs4
import lxml


req = requests.get('https://na.leagueoflegends.com/en-us/news/tags/patch-notes')
req_parsed = bs4.BeautifulSoup(req.text, 'lxml')

#getting a class contains text
text_class = req_parsed.select('time')
print(text_class[0].getText())