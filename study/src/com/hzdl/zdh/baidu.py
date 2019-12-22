#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
#from selenium.common.exceptions import NoSuchElementException
from time import sleep
#from time import ctime
at=webdriver.Firefox()
at.get("https://www.baidu.com")
at.implicitly_wait(20)
mouse=at.find_element_by_link_text("设置")
ActionChains(at).move_to_element(mouse).perform()
at.find_element_by_link_text("搜索设置").click()
# s是下拉框
s=at.find_element_by_id("nr")
#s.find_element_by_xpath("//option[@value='50']").click()
Select(s).select_by_index(1)
sleep(2)
js='document.getElementsByClassName("prefpanelgo")[0].click()'
at.execute_script(js)
sleep(2)
t=at.switch_to_alert()
print(t.text)
sleep(2)
t.accept()