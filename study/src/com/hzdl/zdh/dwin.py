#coding=utf-8
from selenium import webdriver
from time import sleep
profile_directory=r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\pwaxlqc6.default"
profile=webdriver.FirefoxProfile(profile_directory)
driver=webdriver.Firefox(profile)
driver.get("https://www.baidu.com")

js='document.getElementsByClassName("mnav")[0].target=""'
driver.execute_script(js)
sleep(2)

driver.find_element_by_link_text("新闻").click()