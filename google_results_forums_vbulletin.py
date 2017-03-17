# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 11:27:26 2017

@author: hobbyist
"""

import requests
import bs4
import redis


def urlchecker(url):
    try:
        url.index('.ir/')
        return "ir"
    except:
        pass
    
    try:
        url.index('.com/')
        return "com"
    except:
        return "no"
    

        
    


redis = redis.StrictRedis(host='localhost',port=6379,db=0)

for i in range(1,1000):
    print i
    urlpage = "http://parsijoo.ir/web?q=Powered+by+vBulletin++%D9%81%D8%B1%D9%88%D9%85+%D8%A7%D9%86%D8%AC%D9%85%D9%86&acinput=&acvalue=&pq=Powered+by+vBulletin+%D8%A7%D9%86%D8%AC%D9%85%D9%86&co={}0".format(i)
    r= requests.get(urlpage)
    soup = bs4.BeautifulSoup(r.content,"lxml")
    
    for a in soup.find_all("a"):
        try:
           
           url= a['href']
           if url[0:7] == "http://" :
               if url[0:11]!="http://pars":
                   domainkind =urlchecker(url)
                       
                   if domainkind == "ir" :
                           ind =url.index('.ir/')
                           redis.incr(url[0:ind+4])
                           print url[0:ind+4]
                   elif domainkind == "com":
                           ind =url.index('.com/')
                           redis.incr(url[0:ind+5])
                           print url[0:ind+5]   
                           
                   elif domainkind == "no":
                           print "not ir not com"
    
        except:
            print "could'nt get href"
                           
                           
                           
                           
                           
                           