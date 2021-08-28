
import requests
from bs4 import BeautifulSoup
import json
import pprint

def scrape_data():
    url="https://webscraper.io/test-sites"
    page= requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    div=soup.find("div",class_="container test-sites")
    site=div.find_all("div",class_="col-md-7 pull-right")
    print(site)

    list1=[]
    commerce=0
    for i in site:
        commerce=commerce+1
      
        commerce_site=i.find("h2",class_="sit.heading").a.get_text().strip()
        name_sites=commerce_site
        link1=i.find("h2",class_="site.heading").a["href"]
        link2="https://webscraper.io"+[link1]
        h={"commece":commerce,"commerce_site":name_sites,"url1":link2}
        list1.append(h)
        with open("commerce_site.json","w") as file:
            json.dump(list1,file,indent=4)
    return list1
scrape_data()








