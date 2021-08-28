from task2 import *
def group_year():
    decad_year={}
    list12 = []
    for index in realeas_yr():
        m=index%10
        v=index-m
        if v not in list12:
            list12.append(v) #it is created of list of decade
    #print(list12)
    list12.sort()
    for i in list12:
        decad_year[i]=[]
    # x=[]
    print(decad_year)
    for i in list12:
        mj=i+9 #dec10=1659
        for m in d:
            if m<=mj and m>=i:#dec10=1959 or 1950tk chlana hai               
                for n in d[m]:
                    decad_year[i].append(n)
    return decad_year
rs=group_year()
s=open("task3.json","w")
s.write(json.dumps(rs,indent=4))
s.close()
    
group_year()  



