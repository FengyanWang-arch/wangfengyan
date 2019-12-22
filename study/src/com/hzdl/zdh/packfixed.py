#coding=utf-8
from selenium import webdriver
#from selenium.common.exceptions import *
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Firefox()
driver.get("https://www.baidu.com")

def find_element(locator,timeout=10):
    element=WebDriverWait(driver,timeout,1).until(lambda x:x.find_element(*locator))
    return element

input_loc=("id","kw")
button_loc=("id","su")
find_element(input_loc).send_keys("yoyo")
find_element(button_loc).click()