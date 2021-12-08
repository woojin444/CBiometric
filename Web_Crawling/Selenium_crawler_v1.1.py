
# coding: utf-8

# In[32]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib import request
import time
import re
import os


def downloadImages(imageLinks,target):
    os.makedirs('./img/', exist_ok=True)
    name = target.replace('https://www.instagram.com/',"")
    name = name.replace('/',"")
    n = 0
    for i in imageLinks:
        n += 1
        request.urlretrieve(i,"./img/"+name+"["+str(n)+'].jpg')

class InsBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('./chromedriver.exe')

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def getHTML(self,targetURL):
        driver = self.driver
        driver.get(targetURL)
        time.sleep(2)
        postNumber = int(driver.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[1]/span/span').text)
        scrollTimes = (postNumber//24)+1
        time.sleep(1)
        #for i in range(scrollTimes):
        #    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #    time.sleep(2)
        #driver.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[2]/a').click()
        #driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        driver.find_element_by_partial_link_text('followers').click()
        time.sleep(8)
        followersHTML = driver.find_element_by_xpath("//div[@role='dialog']").get_attribute('outerHTML')
        time.sleep(2)
        imagesHTML = driver.find_element_by_xpath("//article").get_attribute('outerHTML')
        time.sleep(2)
        return followersHTML,imagesHTML

    def HTMLtoLinks(self,followersHTML,imagesHTML):
        images = re.findall(r'src="(.+?)"', imagesHTML)
        followers = re.findall(r'href="(.+?)"', followersHTML)
        followers_set = set()
        followers_text = open("followers.txt", "w")
        for i in followers:
            followers_set.add('https://www.instagram.com'+i)
            followers_text.write('https://www.instagram.com'+i+"\n")
        return images,followers_set



target = 'https://www.instagram.com/wu.kris/'
username = "seawind242"
password = "zxc123456"

ib = InsBot(username,password)
ib.login()
followersHTML,imagesHTML = ib.getHTML(target)
images,followers_set = ib.HTMLtoLinks(followersHTML,imagesHTML)
downloadImages(images,target)
ib.closeBrowser()


# while True:
#     try:
#         followersHTML,imagesHTML = ib.getHTML(target)
#         images,followers_set = ib.HTMLtoLinks(followersHTML,imagesHTML)
#         downloadImages(images,target)
#     except Expection:
#         ib.closeBrowser()
#         time.sleep(60)
#         ib = InsBot(username,password)
#         ib.login()
