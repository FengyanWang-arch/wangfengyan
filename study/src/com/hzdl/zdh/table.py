#coding=utf-8
from selenium import webdriver
driver=webdriver.Firefox()
driver.get("file:///C:/Users/Administrator/Desktop/table.html")
s=driver.find_element_by_xpath(".//*[@id='myTable']/tbody/tr[3]/td[1]")
print(s.text)