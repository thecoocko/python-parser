import requests
from bs4 import BeautifulSoup as bs


page = 1

# while page <= 16:
#     pass
#     req = requests.get('https://stopgame.ru/review/new/izumitelno/p'+str(page))
#     html = bs(req.content,'html.parser')
#     for elem in html.select('.items > .article-summary'):
#         pass
#         txt = elem.select('.caption > a')
#         print(txt[0].text)
        

#     page+=1


req = requests.get('https://filmix.ac/filmi/animes/pages/2')
with open('test.html', 'w', encoding='windows-1251') as output_file:
  output_file.write(req.text)

