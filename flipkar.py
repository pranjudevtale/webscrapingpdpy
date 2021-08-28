from os import write
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import time
names=[]
prices=[]
ratings=[]
details=[]
inp=int(input("How many page in scrap in flipkrt(1 to 10)  "))
for i in range(1,inp+1):
    urls=requests.get("https://www.flipkart.com/search?q=mi+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mi+mobiles%7CMobiles&requestId=11d3cd29-43ce-4cd8-8a45-5c6821a17b0d&as-searchtext=mi&page="+str(i))
    soup=BeautifulSoup(urls.text,"html.parser")

    price=soup.find_all(class_="_30jeq3 _1_WHN1")
    name=soup.find_all(class_="_4rR01T")
    rating=soup.find_all(class_="_3LWZlK")
    detail=soup.find_all(class_="col col-7-12")
    for i in price:
        prices.append(i.text)
    for i in name:
        names.append(i.text)
    for i in rating:
        ratings.append(float(i.text))
    for i in detail:
        details.append(i.text)
d={}
list1=[]
for r,a,j,k in zip(names,prices,ratings,details):
    d["Name"]=r
    d["Prices"]=a
    d["Rating"]=j
    d["Details"]=k
    list1.append(d.copy())
import json
s=open("./flipkart2.json","w")
json.dump(list1,s,indent=4)
s.close()