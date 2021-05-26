
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.chrome.service import Service
import time
import random as rd

class SEO:
    def __init__(self):
        self.driver=None
        self.home_path=None
        
    def delay(self,times):
        time.sleep(times)
    def edge(self,object):
        self.driver=webdriver.Edge(executable_path="msedgedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.google.com")
    def chrome(self,object):            
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        if object == None:
            self.driver.get("https://www.google.com")
        else:
            self.driver.get(object)
#    def back(self):        
#        self.driver.back()        
    def quit(self):
        if(self.driver!=None):
            self.driver.quit()
        self.driver=None
    def get_driver(self):
        return self.driver
        
        
    def search(self,key_words):
        self.driver.implicitly_wait(300)
        search_box=self.driver.find_element(By.NAME,'q')
        search_box.click()
        for letter in key_words:
            search_box.send_keys(letter)
            speed=rd.uniform(0,1.5)
            self.delay(speed)
        search_box.send_keys(Keys.ENTER)
    def sc_down(self):
        self.driver.implicitly_wait(300)
        height=self.driver.execute_script("return document.body.scrollHeight")
        for i in range(0,height):
            script="window.scrollTo(0,"+str(i)+")"
            self.driver.execute_script(script)
    def sc_up(self):
        self.driver.implicitly_wait(300)
        height=self.driver.execute_script("return document.body.scrollHeight")
        for i in range(0,height):
            script="window.scrollTo(0,"+str(height-i)+")"
            self.driver.execute_script(script)
    def rank(self):
        for i in range(1,21):
            if(i%10!=0):
                xpath='//*[@id="rso"]/div['+str(i%10)+']'
            else:
                xpath='//*[@id="rso"]/div['+str(10)+']'
            try:
                cite_tag=self.driver.find_element(By.XPATH,xpath+'//cite')
                if "wakame-uit.online" in cite_tag.text:
                    print("Top",i,"trong tìm kiếm của Google")
                    wakame=self.driver.find_element(By.XPATH,xpath+'//a')
                    return i,wakame
                if (i%10==0 and i<20):
                    n_p='//*[@id="pnnext"]'
                    next=self.driver.find_element(By.XPATH,n_p)
                    next.click()                
            except:
                print("rank Failed")
            
        print("Ngoài top 10 trong tìm kiếm Google")
        return None,None
    def toPage(self):
        self.driver.implicitly_wait(10)
        index,page=self.rank()
        if(page != None):
            page.click()
        else:
            print("ToPage Failed")
            return 1/0
            
    def toTop(self):
        self.driver.implicitly_wait(100)
        try:
            back_top_path='//*[@id="back-top"]/a'
            back_top=self.driver.find_element(By.XPATH,back_top_path)
            back_top.click()
        except:
            print("toTop Failed")
        
    def read(self,speed):
        if speed == None:
            spd = 0.008
        else:
            spd= speed
        try:
            self.driver.implicitly_wait(100)
            height=self.driver.execute_script("return document.body.scrollHeight")
            for i in range(0,height):
                script="window.scrollTo(0,"+str(i)+")"
                self.driver.execute_script(script)
                self.delay(spd)
        except :
            print("read Failed")
            pass

    def Home(self):
        try:
            self.driver.implicitly_wait(300)
            home_path='//*[@id="navigation"]/li[1]/a'
            home=self.driver.find_element(By.XPATH,home_path)
            home.click()
        except :
            print("Home Failed")
            pass
    
    def News(self):
        try:
            self.driver.implicitly_wait(300)
            news_path="//*[@id='navigation']/li[3]/a"
            news=self.driver.find_element(By.XPATH,news_path)
            news.click()
        except :
            print("News Failed")
            pass
    
    def search_box(self,key_words):
        try:
            search_box_path="/html/body/main/section[2]/div/div/div[2]/div/aside[1]/form/div/div/input"
            search_box=self.driver.find_element(By.XPATH,search_box_path)
            search_box.click()
            for letter in key_words:
                search_box.send_keys(letter)
                speed=rd.uniform(0,1.5)
                self.delay(speed)
            search_box.send_keys(Keys.ENTER)
        except :
            print("search_box Failed")
            pass
        
    def toContent(self,num):
        n=rd.randint(1,num)
        if(n>4):
            self.sc_down()
            try:
                for i in range(0,n//4):
                    ne='/html/body/main/section[2]/div/div/div[1]/div/nav/ul/li['+str(n//4 +2)+']/a'
                    nex=self.driver.find_element(By.XPATH,ne)
                    nex.click()
            except:
                print("next page Failed")
                pass
                
        if(n%4!=0):
            p='/html/body/main/section[2]/div/div/div[1]/div/article['+str(n%4)+']/div[2]/a'
        else:
            p='/html/body/main/section[2]/div/div/div[1]/div/article[4]/div[2]/a'
        try:
            h=self.driver.find_element_by_xpath(p)  
            h.click()         
        except:
            print("toContent Failed")
            pass
        
    def Courses(self):
        try:
            self.driver.implicitly_wait(300)
            courses_path='//*[@id="navigation"]/li[2]/a'
            courses=self.driver.find_element(By.XPATH,courses_path)
            courses.click()
        except :
            print("Courses Failed")
    
    def About(self):
        try:
            self.driver.implicitly_wait(300)
            aboutus_path='//*[@id="navigation"]/li[4]/a'
            aboutus=self.driver.find_element(By.XPATH,aboutus_path)
            aboutus.click()
        except:
            print("About Failed")
            pass
        