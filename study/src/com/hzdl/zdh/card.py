#coding=utf-8
from selenium import webdriver
from time import sleep
profile_directory=r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\pwaxlqc6.default"
profile=webdriver.FirefoxProfile(profile_directory)
driver=webdriver.Firefox(profile)
driver.get("https://www.12306.cn/index/")
js='document.getElementById("train_date").removeAttribute("readonly")'
driver.execute_script(js)
sleep(2)
#driver.find_element_by_id("train_date").clear()
#sleep(3)
#driver.find_element_by_id("train_date").send_keys("2019-11-16")
js_value='document.getElementById("train_date").value="好好学习"'
driver.execute_script(js_value)
