# internet speed test bot and complain in twitter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import   NoSuchElementException
import time
do=webdriver.ChromeOptions()
do.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=do)
# to get internet speed
driver.get(url="https://www.speedtest.net/")
# click button to accept privacy
pb=driver.find_element(By.CSS_SELECTOR,value="#onetrust-accept-btn-handler")
pb.click()
#click for go
gob=driver.find_element(By.CSS_SELECTOR,value="#container > div.pre-fold > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.start-button > a > span.start-text")
gob.click()
#finding upload and download speed
now=time.time()
af3m=now+300
a=True
dmbbs=40
upmbbs=15
while(a):
    if time.time()>=af3m:
        dummy1=driver.find_element(By.XPATH,value="//*[@id='container']/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
        dmbbs=dummy1.text
        dummy2=driver.find_element(By.XPATH,value="//*[@id='container']/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        upmbbs=dummy2.text
        print(dmbbs,upmbbs)
        break
# comment on twitter
#sign in on twiiter
driver.get("https://x.com/?lang=en")
ts=driver.find_element(By.XPATH,value="//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div")
ts.click()
# log in popup
a=True
now=time.time()
aft3m=now+180
aft5m=now+300
while(a):
    if time.time()>=aft3m:
        email = driver.find_element(By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input")
        email.send_keys( "your email id")
        next1 = driver.find_element(By.XPATH,value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div")
        next1.click()
        break
while(a):
    if time.time()>=aft5m:
        try:
            password = driver.find_element(By.XPATH, value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
            password.send_keys("your password")
            login = driver.find_element(By.XPATH,value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/button/div")
            login.click()
            break
        except NoSuchElementException:
            username=driver.find_element(By.XPATH,value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
            username.send_keys("your user na,e")
            next2=driver.find_element(By.XPATH,value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button/div")
            next2.click()
            now2=time.time()
            aft3m2=now2+45
            while(a):
                if time.time()>aft3m2:
                    password1=driver.find_element(By.XPATH,value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
                    password1.send_keys("your password")

                    login1 = driver.find_element(By.XPATH,value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/button")
                    login1.click()
                    break
            break
#making post
nowl=time.time()
af2m=nowl+120
while(a):
    if time.time()>af2m:
        posti = driver.find_element(By.CSS_SELECTOR,value="#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div > div > div.css-175oi2r.r-kemksi.r-184en5c > div > div.css-175oi2r.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(1) > div > div > div > div > div > div > div > div > div > div > div > div.css-175oi2r.r-1wbh5a2.r-16y2uox > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div > span")
        posti.send_keys(" jio net speed slow then what you promissed @your desired person ")
        postb = driver.find_element(By.CSS_SELECTOR, value="#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div > div > div.css-175oi2r.r-kemksi.r-184en5c > div > div.css-175oi2r.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-175oi2r.r-kemksi.r-jumn1c.r-xd6kpl.r-gtdqiz.r-ipm5af.r-184en5c > div:nth-child(2) > div > div > div > button")
        postb.click()
        break
