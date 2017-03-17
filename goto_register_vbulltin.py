# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 12:50:32 2017

@author: hobbyist
"""

import redis
import shopkeeper_commenter


myredis = redis.StrictRedis(host='localhost',port=6379,db=0)



for page in range(20000,20010):


            shopkeeper_commenter.fuckit("http://forum.shopkeeper.ir/register.php",page)



#keys =myredis.keys()
#
#for key in keys :
#    myurl = key +"register.php"
#    shopkeeper_commenter.fuckit(myurl)
#    
#    
#    
#    
    
    
    