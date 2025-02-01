import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
co=ChromeOptions()
co.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=co)
# get the data from zillow clone website
al=[]
ll=[]
pl=[]
zillowcloneurl="https://appbrewery.github.io/Zillow-Clone/"
driver.get(zillowcloneurl)
time.sleep(60)
houselist=driver.find_elements(By.XPATH,value="//*[@id='grid-search-results']/ul/li")
l=(len(houselist))
print(l)
for i in range(1,l+1):
    addres = f"/html/body/div/div[2]/div/div/div[1]/div[1]/div/ul/li[{i}]/div/div/article/div/div[1]/a/address"
    dummy1=driver.find_element(By.XPATH,value=addres)
    al.append(dummy1.text)
    dummy2=driver.find_element(By.XPATH,value=f"/html/body/div/div[2]/div/div/div[1]/div[1]/div/ul/li[{i}]/div/div/article/div/div[1]/div[2]/div/span")
    pl.append(dummy2.text)
    dummy3=driver.find_element(By.XPATH,value=f"/html/body/div/div[2]/div/div/div[1]/div[1]/div/ul/li[{i}]/div/div/article/div/div[1]/a")
    ll.append(dummy3.get_attribute("href"))
print(al)
# put the data to form
formurl="form url"
l=len(al)

for i in range(0,l):

    driver.get(formurl)
    time.sleep(120)
    adr=driver.find_element(By.XPATH,value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")

    adr.send_keys(al[i])
    rent=driver.find_element(By.XPATH,value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    rent.send_keys(pl[i])
    lli=driver.find_element(By.XPATH,value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    lli.send_keys(ll[i])
    submit=driver.find_element(By.XPATH,value="//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
    submit.click()







