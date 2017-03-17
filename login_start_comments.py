# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 16:56:35 2017

@author: hobbyist
"""





from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def login_start_commenting(browser,login_userrname,login_password,commentpage):
            
            browser.get("http://forum.shopkeeper.ir/forum.php")
                        
            browser.execute_script("document.getElementById('navbar_password').style.display = 'inline';")
            user =browser.find_element_by_id('navbar_username')
            puss =browser.find_element_by_id('navbar_password')
            voroood =browser.find_element_by_xpath('//*[@id="logindetails"]/div/div/input[4]')
            
            
            user.send_keys(login_userrname)
            puss.send_keys(login_password)
            time.sleep(1)
            voroood.click() 
            time.sleep(1)
            
            try:
                WebDriverWait(browser, 10).until(EC.alert_is_present(),
                                               'Timed out waiting for PA creation ' +
                                               'confirmation popup to appear.')
            
                alert = browser.switch_to_alert()
                alert.dismiss()
                print "alert dismissed"
            except TimeoutException:
                print "no alert"
            
                
            try:
                    urlposts="http://forum.shopkeeper.ir/showthread.php?t="+str(commentpage)
                    browser.get(urlposts)
                    textarea =browser.find_element_by_xpath('//*[@id="cke_contents_vB_Editor_QR_editor"]/textarea')
                    textarea.send_keys("salamیک سوال در مورد راه اندازی فروشگاه داشتم. ممکنه راهنمایی کنید؟ ")
                    su =browser.find_element_by_xpath('//*[@id="qr_submit"]')
                    time.sleep(2)
                    su.click()
                    time.sleep(32)
                    
            except Exception as e:
                time.sleep(1)
                print str(e)