#coding=utf-8
from selenium import webdriver
from time import sleep
profile_directory=r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\pwaxlqc6.default"
profile=webdriver.FirefoxProfile(profile_directory)
driver=webdriver.Firefox(profile)
driver.get("http://www.baidu.com")
sleep(2)
text=driver.find_element_by_id("setf").text
print(text)
tag=driver.find_element_by_igkd("kw").tag_name
print(tag)
sleep(2)
name=driver.find_element_by_id("kw").get_attribute("class")
print(name)
sleep(2)
driver.find_element_by_id("kw").send_keys("yoyoketang")
value=driver.find_element_by_id("kw").get_attribute("value")
print(value)
print(driver.name)