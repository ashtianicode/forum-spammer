# -*- coding: utf-8 -*-
# tor browser config :
#from tbselenium.tbdriver import TorBrowserDriver
#with TorBrowserDriver("/home/hobbyist/Desktop/tor-browser_en-US/") as browser:


from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import random
import time
import string
import make_fake_email
import login_start_comments
import selenium.webdriver as webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
def randtext(size=6 ,chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



def register(urlforum):
                randemailtext=randtext()
                text = "شاپ کیپر"
                browser = webdriver.Chrome('/home/taha/Documents/playground/selenium/chromedriver',chrome_options=chrome_options)
                e =randemailtext +"@stop-my-spam.pp.ua"
                print e
                newurl = urlforum
                browser.get(newurl) 
                
                username =browser.find_element_by_id('regusername')
                password =browser.find_element_by_id('password')
                password2 =browser.find_element_by_id('passwordconfirm')
                email =browser.find_element_by_id('email')
                email2 =browser.find_element_by_id('emailconfirm')
                Q=browser.find_element_by_id('humanverify')
                phone =browser.find_element_by_id('cfield_7')
                check =browser.find_element_by_xpath('//*[@id="registerform"]/div[2]/div/div[2]/label')
                submit =browser.find_element_by_xpath('//*[@id="registerform"]/div[3]/div/input[10]')
                
                login_userrname= randtext()
                login_password = randtext()
                username.send_keys(login_userrname)
                password.send_keys(login_password)
                password2.send_keys(login_password)
                email.send_keys(e)
                email2.send_keys(e)
                Q.send_keys(text)
                phone.send_keys("09126278390")
                time.sleep(3)
                check.click()
                submit.click()
                browser.delete_all_cookies()
                
                print "submit clicked"
                message=""
                while (  message==""):
                            try:
                                
                                    message =browser.find_element_by_xpath('//*[@id="vbulletin_html"]/body/div[2]/div[3]/h2').text
                                    print message
                
                
                            
                            except:
                                    print"submit not done"
                                    time.sleep(1)
                return {'randemailtext':randemailtext,'login_userrname':login_userrname,'login_password':login_password,'browser':browser}




def fuckit(urlforum,commentpage):
    


            registerout =register(urlforum)
            randemailtext = registerout['randemailtext']
            browser = registerout['browser']
            login_userrname = registerout['login_userrname']
            login_password = registerout['login_password']
            
            
            # click on mail activation link
            make_fake_email.getfakeemail(randemailtext,browser)
            
            
            
            #login
            login_start_comments.login_start_commenting(browser,login_userrname,login_password,commentpage)
            





