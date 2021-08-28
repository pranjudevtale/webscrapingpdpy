from task import *
import json
# from pprint import pprint
def realeas_yr():
    year=[]
    for i in scrape_top_list():
        for j in i:
            if i['year'] not in year:
                year.append(i['year'])
    year=sorted(year)
    movie_dict={i:[] for i in year}
    for i in scrape_top_list():
        yr=i['year']
        for x in movie_dict:
            if str(x)==str(yr):
                movie_dict[x].append(i)
    return movie_dict
d=realeas_yr()
f=open('task2.json', 'w')
f.write(json.dumps(d,indent=4))
f.close()








  