# set face book account
import time
fm="your gmail"
fp="your password"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
do=webdriver.ChromeOptions()
do.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=do)
# log into tinder
tinderurl="https://tinder.com/"
driver.get(tinderurl)
time.sleep(30)
# clicking accept key
acc=driver.find_element(By.XPATH,value="//*[@id='t-1364086984']/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]/div")
acc.click()
login=driver.find_element(By.XPATH,value="//*[@id='t-1364086984']/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div")
login.click()
time.sleep(30)
moreop=driver.find_element(By.XPATH,value="//*[@id='t-1142746548']/div/div/div/div[1]/div/div/div[2]/div[2]/span/button")
moreop.click()
loginwfb=driver.find_element(By.XPATH,value="//*[@id='t-1142746548']/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div")
loginwfb.click()
time.sleep(60)
d1=driver.window_handles
print(len(d1))
driver._switch_to.window(d1[1])
time.sleep(60)
# log in pop up
email=driver.find_element(By.XPATH,value="//*[@id='email']")
email.send_keys(fm)
password=driver.find_element(By.XPATH,value="//*[@id='pass']")
password.send_keys(fp)
time.sleep(80)
fbli=driver.find_element(By.XPATH,value="//*[@id='loginbutton']")
fbli.send_keys(Keys.ENTER)
time.sleep(30)
print(len(driver.window_handles))
driver._switch_to.window(driver.window_handles[1])

# incase previous login
time.sleep(60)
print(driver.title)
continu=driver.find_element(By.CSS_SELECTOR,value="#mount_0_0_sh > div > div > div > div > div > div > div.x9f619.x1ja2u2z.x78zum5.x1q0g3np.x1iyjqo2.x1t2pt76.x1n2onr6.xvrxa7q.x1nhjfyr > div.x9f619.x2lah0s.x1n2onr6.x78zum5.x1iyjqo2.x1t2pt76.x1lspesw > div > div > div > div > div > div > div.x9f619.x78zum5.xdt5ytf.x2lah0s.x193iq5w.x1l90r2v.xexx8yu.x2bj2ny.x1ey2m1c.xixxii4.x80663w.xh8yej3.x1vjfegm > div > div > div.x1n2onr6.x1ja2u2z.x9f619.x78zum5.xdt5ytf.x2lah0s.x193iq5w.xyamay9 > div > div > div > div:nth-child(1) > div > div > div > div > div > div.x6s0dn4.x78zum5.xl56j7k.x1608yet.xljgi0e.x1e0frkt > div > span > span")
continu.click()
time.sleep(120)
#tinder area
# switch to base window
driver._switch_to.window(driver.window_handles[0])
allow=driver.find_element(By.XPATH,value="//*[@id='t-1142746548']/div/div/div/div/div[3]/button[1]/div[2]/div[2]/div")
allow.click()
time.sleep(30)
la=driver.find_element(By.XPATH,value="//*[@id='t-1142746548']/div/div/div/div/div[3]/button[2]/div[2]/div[2]/div")
la.click()
time.sleep(30)
cat=driver.find_element(By.XPATH,value="//*[@id='mount_0_0_gX']/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div/div[1]/div/span/span")
cat.click()
time.sleep(30)
for i in range(0,100):
    wrong=driver.find_element(By.XPATH,value="//*[@id='t-1364086984']/div/div[1]/div/div/div/main/div/div/div/div/div[4]/div/div[2]/button/span/span[1]/svg")
    wrong.click()
    time.sleep(30)
