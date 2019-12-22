#coding=utf-8
from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get("https://mail.163.com/")
driver.implicitly_wait(5)
s=driver.find_element_by_id("switchAccountLogin")
s.click()
sleep(1)
#driver.switch_to_frame("x-URS-iframe1573281490621.767")
#driver.find_element_by_name("email").send_keys("123")
#driver.find_element_by_name("password").send_keys("456")
#driver.switch_to.default_content()