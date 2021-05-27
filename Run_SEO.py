#!/usr/bin/env python
# coding: utf-8

# In[1]:


# TRƯỚC TIÊN HÃY CÀI CÁC GÓI PACKAGES SAU ĐÂY BẰNG LỆNH DƯỚI ĐÂY #
#             pip install selenium, wmi, netifaces               #

# class SEO:
#     def __init__(self):
#         self.driver=None
#         self.home_path=None
#         pass
#     def delay(self,times):
#         time.sleep(times)
#     def edge(self,object):
#         self.driver=webdriver.Edge(executable_path="msedgedriver.exe")
#         self.driver.maximize_window()
#         self.driver.get("https://www.google.com")
#     def chrome(self,object):            
#         self.driver=webdriver.Chrome()
#         self.driver.maximize_window()
#         if object == None:
#             self.driver.get("https://www.google.com")
#         else:
#             self.driver.get(object)
#     def back(self):
        
#         self.driver.back()        
#     def quit(self):
#         self.driver.quit()
#         self.driver=None
#     def get_driver(self):
#         return self.driver
        
        
#     def search(self,key_words):
#         self.driver.implicitly_wait(300)
#         search_box=self.driver.find_element(By.NAME,'q')
#         search_box.click()
#         for letter in key_words:
#             search_box.send_keys(letter)
#             speed=rd.uniform(0,1.5)
#             self.delay(speed)
#         search_box.send_keys(Keys.ENTER)
#     def sc_down(self):
#         self.driver.implicitly_wait(300)
#         height=self.driver.execute_script("return document.body.scrollHeight")
#         for i in range(0,height):
#             script="window.scrollTo(0,"+str(i)+")"
#             self.driver.execute_script(script)
#     def sc_up(self):
#         self.driver.implicitly_wait(300)
#         height=self.driver.execute_script("return document.body.scrollHeight")
#         for i in range(0,height):
#             script="window.scrollTo(0,"+str(height-i)+")"
#             self.driver.execute_script(script)
#     def rank(self,object):
#         if object == None:
#             href="https://wakame-uit.online"
#         for i in range(1,10):
#             xpath="//*[@id='rso']/div["+str(i)+"]/div/div/div[1]/a"
#             wakame=self.driver.find_element(By.XPATH,xpath)
#             if(wakame.get_attribute('href')=="https://wakame-uit.online/"):
#                 print("Top",i,"trong tìm kiếm của Google")
#                 return i,wakame
#         print("Ngoài top 10 trong tìm kiếm Google")
#         return None,None
#     def toPage(self):
#         self.driver.implicitly_wait(300)
#         index,page=self.rank(self)
#         if(page != None):
#             page.click()
            
#     def toTop(self):
#         self.driver.implicitly_wait(300)
#         back_top_path='//*[@id="back-top"]/a'
#         back_top=self.driver.find_element(By.XPATH,back_top_path)
#         back_top.click()
        
#     def read(self):
#         self.driver.implicitly_wait(300)
#         height=self.driver.execute_script("return document.body.scrollHeight")
#         for i in range(0,height):
#             script="window.scrollTo(0,"+str(i)+")"
#             self.driver.execute_script(script)
#             self.delay(0.08)

#     def Home(self):
#         self.driver.implicitly_wait(300)
#         home_path='//*[@id="navigation"]/li[1]/a'
#         home=self.driver.find_element(By.XPATH,home_path)
#         home.click()
    
#     def News(self):
#         self.driver.implicitly_wait(100)
#         news_path="//*[@id='navigation']/li[4]/a"
#         news=self.driver.find_element(By.XPATH,news_path)
#         news.click()
    
#     def search_box(self,key_words):
#         search_box_path="/html/body/main/section[2]/div/div/div[2]/div/aside[1]/form/div/div/input"
#         search_box=self.driver.find_element(By.XPATH,search_box_path)
#         search_box.click()
#         for letter in key_words:
#             search_box.send_keys(letter)
#             speed=rd.uniform(0,1.5)
#             self.delay(speed)
#         search_box.send_keys(Keys.ENTER)
# #    def ToContent(self):
# #        self.driver.implicitly_wait(100)
# #        content_path='/html/body/main/section[2]/div/div/div[2]/div/aside[3]/div/div/a'
# #        content=self.driver.find_element(By.XPATH,content_path)
# #        content.click()
        
#     def Courses(self):
#         self.driver.implicitly_wait(300)
#         courses_path='//*[@id="navigation"]/li[2]/a'
#         courses=self.driver.find_element(By.XPATH,courses_path)
#         courses.click()
    
#     def About(self):
#         self.driver.implicitly_wait(300)
#         aboutus_path='//*[@id="navigation"]/li[5]/a'
#         aboutus=self.driver.find_element(By.XPATH,aboutus_path)
#         aboutus.click()
# In[2]:


import pandas as pd
import time,datetime
import random as rd
from change_ip_mac import IP_MAC
from SEO import SEO


# In[3]:


# TRƯỚC TIÊN HÃY CÀI CÁC GÓI PACKAGES SAU ĐÂY BẰNG DƯỚI ĐÂY #
# pip install selenium, wmi, netifaces #

####### Khởi tạo #######
a=SEO()
fake=IP_MAC()
report=pd.DataFrame(columns=[
    'Lần', 'Trạng thái', 'Địa chỉ IP', 
    'Địa chỉ MAC','Thời gian SEO',"Key_words"
])
########################


#Danh sách từ khóa (thương hiệu, thương mại)
KEYWORDS=["Clb Wakame","wakame uit","uit wakame","luyện thi jlpt wakame UIT",
          "tin tức Wakame","các khóa học của wakame"
         ]
#Tổng số bài đăng trên web hiện tại
MAX=7
#Số lần thực hiện truy cập trang web
sl_truycap=2

#Khoảng thời gian dừng ở lại trang (không làm gì) từ 5s tới 20s tùy mọi setup
WAIT=[10,30]

#Random thời gian
def t():
    return rd.randint(WAIT[0],WAIT[1])


# In[4]:


for i in range(sl_truycap):
    keywords="-----------"
    try:
        #Thay đổi IP và MAC
        fake.__init__()
        fake.run()
        
        #Search từ khóa
        a.delay(5)
        a.chrome(None)
        a.delay(5)
        keywords=KEYWORDS[rd.randint(0,len(KEYWORDS)-1)]
        #keywords='các khóa học wakame'
        print(keywords)
        a.search(keywords) #Random từ khóa ngẫu nhiên
        a.delay(5)
        #a.search("Luyện thi JLPT Wakame")
        
        #Phần thao tác trên cửa trang tìm kiếm (Option)
        a.sc_down() #Cuộn trang xuống
        a.delay(3)
        a.sc_up()
        
        a.toPage() #Vào trang của mình (https://wakame-uit.online)
        #a.quit()
        
        st=time.time()    
        #Phần thao tác trên trang Wakame
        a.delay(5)
        
        a.sc_down()
        
        a.delay(t())
        
        a.toTop()
        
        a.delay(t())

        a.Home()         # Đi tới trang Tin tức
        
        a.sc_down()
        
        a.delay(5)
        
        a.News()
        
        a.delay(5)

        a.search_box("Văn hóa") #Chỉ thực hiện được khi đã ở trang Tin tức
        
        a.delay(5)

        a.News()         # Quay lại trang trước
        
        a.delay(t())
        
        a.toContent(MAX) # Chọn bài báo ngẫu nhiên để click (chỉ khi ở trang Tin tức)
        
        a.read(0.01)
        
        a.delay(t())
        
        a.News()
        
        a.delay(t())
        
        a.toContent(MAX)
        
        a.read(0.01)
        
        a.toTop()
        
        a.delay(t())
        #### Kết thúc SEO ##
        fake.is_connect()
        
        a.quit()
        print("\n#### SEO lần",i+1,"thành công ####\n")
                
        report.loc[i]=[i+1,"Success",fake.get_IP(),fake.get_MAC(),str(datetime.timedelta(seconds=time.time()-st)),keywords]
    except:
        a.quit()
        report.loc[i]=[i+1,"Failed","---.---.---.---","--.--.--.--.--.--","--:--:--",keywords]
        print("\n#### SEO lần",i+1,"thất bại ####\n")


# In[5]:


report


# In[ ]:





# In[ ]:




