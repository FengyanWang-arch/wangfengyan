#coding=utf-8
from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get("file:///C:/Users/Administrator/Desktop/checkbox.html")
s=driver.find_element_by_id("boy").is_selected()
print(s)
driver.find_element_by_id("boy").click()
r=driver.find_element_by_id("boy").is_selected()
print(r)

driver.find_element_by_id("c2").click()
sleep(3)
checkboxs=driver.find_elements_by_xpath(".//*[@type='checkbox']")
for i in checkboxs:
    i.click()