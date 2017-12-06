import requests
from bs4 import BeautifulSoup
import json

id = 0
def spider(year):
    global id
    movie_details = {}
    page = 1
    max_pages = 2
    while page <= max_pages:
        print(page)
        url = 'http://www.imdb.com/search/title?release_date='+str(year)+'&page='+str(page)+'&ref_=adv_nxt'
        source_code = requests.get(url, allow_redirects=False)
        soup = BeautifulSoup(source_code.text,'html.parser')
        movies = soup.find_all('div', class_ = 'lister-item mode-advanced')
        for movie in movies:
            name = movie.h3.a.text
            descrption = movie.find_all('p',class_ = 'text-muted')[1].text
            movie_details[id]= {'name':name,'year':year,'plot':descrption}
            id+=1
        page+=1
    with open('json/'+str(year)+'.json','w') as fp:
        json.dump(movie_details,fp,indent=4)

spider(2017)