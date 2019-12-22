#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep
profile_directory=r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\pwaxlqc6.default"
profile=webdriver.FirefoxProfile(profile_directory)
driver=webdriver.Firefox(profile)
driver.get("https://www.baidu.com")
sleep(2)
mouse=driver.find_element_by_link_text("设置")
sleep(2)
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text("搜索设置").click()
sleep(2)
s=driver.find_element_by_id("nr")
sleep(2)
Select(s).select_by_visible_text("每页显示50条")
sleep(2)
#s.click()
#sleep(2)
#driver.find_element_by_id("gxszButton").click()
#driver.find_element_by_link_text("保存设置").click()
js='document.getElementsByClassName("prefpanelgo")[0].click()'
driver.execute_script(js)
sleep(2)
t=driver.switch_to_alert()
print(t.text)
sleep(2)
t.accept()