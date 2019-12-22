#coding=utf-8
from selenium import webdriver

driver1=webdriver.Firefox()
driver1.get("https://www.baidu.com")
print(driver1.title)

driver2=webdriver.Firefox()
driver2.get("http://127.0.0.1:81/t18bbs/forum.php")
print(driver2.title)

driver1.quit()

driver2.find_element_by_id("ls_username").send_keys("wfy")
driver2.find_element_by_id("ls_password").send_keys("111111")
driver2.find_element_by_xpath(".//*[@id='lsform']/div/div/table/tbody/tr[2]/td[3]/button").click()