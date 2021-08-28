
import requests
from bs4 import BeautifulSoup
import json
import pprint
URL = 'https://www.imdb.com/india/top-rated-indian-movies/'
page= requests.get(URL)
soup = BeautifulSoup(page.text,"html.parser")
def scrape_top_list():
    main_div=soup.find("div",class_="lister")
    tbody=main_div.find("tbody",class_="lister-list")
    trs=tbody.find_all("tr")
    movie_rank=[]
    movie_name=[]
    year_of_realease=[]
    movie_url=[]
    movie_rating=[]
    for tr in trs:
        position=tr.find("td",class_="titleColumn").get_text().strip()
        rank=' '
        for i in position:
            if '.' not in i:
                rank=rank+i
            else:
                break
        movie_rank.append(rank)
        title=tr.find("td",class_="titleColumn").a.get_text()
        movie_name.append(title)
        year=tr.find("td",class_="titleColumn").span.get_text()
        year_of_realease.append(year)

        rating=tr.find("td",class_="ratingColumn imdbRating").strong.get_text()
        movie_rating.append(rating)
        link=tr.find("td",class_="titleColumn").a["href"]
        movie_link="https://www.imdb.com"+link
        movie_url.append(movie_link)

    Top_movie=[]
    details={'position':'',"name":'','year':'','rating':'','url':''}
    for i in range(0,len(movie_rank)):
        details['position']=int(movie_rank[i])
        details['name']=str(movie_name[i])
        year_of_realease[i]=year_of_realease[i][1:5]
        details['year']=int(year_of_realease[i])
        details['rating']=float(movie_rating[i])
        details['url']=movie_url[i]
      
        Top_movie.append(details)
        details={'position':'',"name":'','year':'','rating':'','url':''}
        with open("p*.json","w") as file:
            json.dump(Top_movie,file,indent=2)
    return Top_movie


pprint.pprint(scrape_top_list())