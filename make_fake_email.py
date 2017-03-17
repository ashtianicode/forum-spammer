# -*- coding: utf-8 -*-
import time




        

def getfakeemail(randemailtext,browser):        
        
        baseurl = "https://email-fake.com/stop-my-spam.pp.ua/"+ randemailtext
       # browser = webdriver.Chrome('/home/taha/Documents/playground/selenium/chromedriver')
        
        
        #wait for email to get recieved
        browser.get(baseurl) 
        active=False
        while(not active):
            try:
                active =browser.find_element_by_xpath('//*[@id="email-table"]/div[3]/div[4]/div/p/a[1]')
                active.click()
            except:
                browser.get(baseurl) 
        
                print "activation email has not been recieved!"
                time.sleep(1)
               
        #wait for the acount to get activated

        
