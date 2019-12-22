#coding=utf-8
from selenium import webdriver
from time import sleep
#profile_directory=r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\pwaxlqc6.default"
#profile=webdriver.FirefoxProfile(profile_directory)
driver=webdriver.Chrome()
driver.get("https://www.cnblogs.com/yoyoketang")
sleep(2)
js="window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)
sleep(2)
js="window.scrollTo(0,0)"
driver.execute_script(js)
sleep(2)