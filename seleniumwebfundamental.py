from selenium import webdriver
from selenium.webdriver.common.by import By
croptions=webdriver.ChromeOptions()
croptions.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=croptions)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
na=driver.find_element(By.CSS_SELECTOR,value="#articlecount > ul > li:nth-child(2) > a:nth-child(1)")
na.click()
# input to element
driver.get("https://secure-retreat-92358.herokuapp.com/")
fn=driver.find_element(By.NAME,value="fName")
fn.send_keys("dummy1")
fn=driver.find_element(By.NAME,value="lName")
fn.send_keys("dummy2")
fn=driver.find_element(By.NAME,value="email")
fn.send_keys("dummy@3")
fn=driver.find_element(By.CSS_SELECTOR,value="body > form > button")
fn.click()
