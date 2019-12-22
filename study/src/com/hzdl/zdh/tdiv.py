#coding=utf-8
from selenium import webdriver
from time import sleep
profile_directory=r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\pwaxlqc6.default"
profile=webdriver.FirefoxProfile(profile_directory)
driver=webdriver.Firefox(profile)
driver.get("file:///C:/Users/Administrator/Desktop/div.html")
sleep(5)

#js1='document.getElementById("yoyoketang").scrollTop=10000'
#driver.execute_script(js1)
#
#sleep(5)
#
#js2='document.getElementById("yoyoketang").scrollTop=0'
#driver.execute_script(js2)
#sleep(5)
#
#js3='document.getElementById("yoyoketang").scrollLeft=10000'
#driver.execute_script(js3)
#sleep(5)
#
#js4='document.getElementById("yoyoketang").scrollLeft=0'
#driver.execute_script(js4)

#js5='document.getElementByClassName("scroll")'
#print(js5)
#sleep(2)
js6='document.getElementsByClassName("scroll")[0].scrollTop=10000'
driver.execute_script(js6)
sleep(5)

js7='document.getElementsByClassName("scroll")[0].scrollLeft=10000'
driver.execute_script(js7)
