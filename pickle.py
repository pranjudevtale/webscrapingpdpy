import requests
import json
from bs4 import BeautifulSoup

def pickle_task():
    url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
    page=requests.get(url)
    # print(page)
    # html=page.content
    # print(html)
    soup=BeautifulSoup(page.text,"html.parser")
    # print(soup)
    div=soup.find("div",class_="_1gX7")
    # print(div)
    # div=soup.find_all("div",class_="_3RA-")
    # print(div)
    div2=div.span.get_text()
    list=[]
    # print(div2)
    pickle=div2.split(" ")
    # print(pickle)
    split=int(pickle[1])
    print(split)
    split1=split//32+1
    print(split1)
    a=[]
    position=0
    k=1
    while k<=split:
        url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
        api=requests.get(url)
        # print(api)
        soup=BeautifulSoup(api.text,"html.parser")
        # print(soup)
        main_div=soup.find("div",class_="_3RA-")
        # print(main_div)
        div=main_div.find_all("div",class_="UGUy")
        # print(div)
        pickle_price=main_div.find_all("div",class_="_1kMS")
        # print(pickle_price)
        pickle_link=main_div.find_all("div",class_="_3WhJ")
        # print(pickle_link)
        
        i=0
        while i<len(pickle_link):
            position+=1
            pickle_name=div[i].get_text()
            price=pickle_price[i].get_text()
            link=(pickle_link[i].a["href"])
            link1="https://paytmmall.com"+link
            dict={"position":position,"pickle_name":pickle_name,"link":link1,"price":price}
            a.append(dict)
            i=i+1
        k=k+1

        with open("pickle_task.json","w") as f:
            json.dump(dict,f,indent=4)
        return(a)
pickle_task()






