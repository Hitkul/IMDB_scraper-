import requests
from bs4 import BeautifulSoup


def spider(year):
    page = 1
    max_pages = float('Inf')
    while page <= max_pages:
        print(page)
        url = 'http://www.imdb.com/search/title?release_date='+str(year)+'&page='+str(page)+'&ref_=adv_nxt'
        source_code = requests.get(url, allow_redirects=False)
        soup = BeautifulSoup(source_code.text,'html.parser')
        page_number = soup.find('div',class_ = 'desc')
        page_number_text = page_number.text
        max_pages = int(page_number_text[page_number_text.index("of ")+3:page_number_text.index("titles")].replace(",",""))
        movies = soup.find_all('div', class_ = 'lister-item mode-advanced')
        for movie in movies:
            name = movie.h3.a.text
            descrption = movie.find_all('p',class_ = 'text-muted')[1].text
            print(name)
            print(descrption)
            print("--------------------")



spider(2017)