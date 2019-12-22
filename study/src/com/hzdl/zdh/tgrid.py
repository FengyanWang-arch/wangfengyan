#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep


lists={'http://127.0.0.1:4444/wd/hub':"chrome",'http://127.0.0.1:5555/wd/hub':'firefox'}
for key,value in lists.items():
    driver=webdriver.Remote(command_executor=key,desired_capabilities={'platform':'ANY',
                                                                       'browserName':value,
                                                                       'version':'',
                                                                       'javascriptEnabled':True})

    driver.get("https://www.baidu.com")
    driver.find_element_by_id("kw").send_keys("hello")
    driver.find_element_by_id("su").click()
    sleep(2)