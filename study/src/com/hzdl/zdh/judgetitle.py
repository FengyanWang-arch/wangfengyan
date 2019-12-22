#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Firefox()
driver.get("https://www.cnblogs.com/yoyoketang")
#print(driver.title)
title=EC.title_is(r'上海-悠悠 - 博客园')
print(title(driver))
title1=EC.title_contains(r'上海-悠悠')
print(title1(driver))

r1=EC.title_is(r'上海-悠悠 - 博客园')(driver)
r2=EC.title_contains(r'上海-悠悠')(driver)
print(r1)
print(r2)