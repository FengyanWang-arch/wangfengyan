#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver=webdriver.Firefox()
driver.get("https://www.cnblogs.com/yoyoketang/")
try:
    t=driver.find_element_by_id("blog_nav_newpostxx")
except NoSuchElementException as msg:
    print("查找元素异常%s"%msg)
else:
    t.click()