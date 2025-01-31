# internet speed test bot and complain in twitter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import   NoSuchElementException
import time
do=webdriver.ChromeOptions()
do.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=do)
# login to instagram
driver.get(url="link of targeted instagram acount")
time.sleep(120)
username=driver.find_element(By.XPATH,value="//*[@id='loginForm']/div[1]/div[1]/div/label/input")
username.send_keys("your username")
password=driver.find_element(By.XPATH,value="//*[@id='loginForm']/div[1]/div[2]/div/label/input")
password.send_keys("your password")
login=driver.find_element(By.XPATH,value="//*[@id='loginForm']/div[1]/div[3]/button")
login.click()
# click follow button for followers
time.sleep(300)
print(len(driver.window_handles))
notnow=driver.find_element(By.XPATH,value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div")
notnow.click()
time.sleep(780)
followers=driver.find_element(By.XPATH,value="//*[@id='mount_0_0_g1']/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a/span")
print(len(driver.window_handles))
driver.switch_to(driver.window_handles[1])
time.sleep(150)
followersl=driver.find_elements(By.XPATH,value="/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div")
l=len(followersl)
for j in range(1,l+1):
    time.sleep(15)
    dummy1=driver.find_element(By.XPATH,value=f"/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{j}]/div/div/div/div[3]/div")
    dummy1.click()

