#coding=utf-8
from selenium import webdriver
#from time import sleep
profile_directory=r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\pwaxlqc6.default"
profile=webdriver.FirefoxProfile(profile_directory)
driver=webdriver.Firefox(profile)
driver.get("https://www.cnblogs.com/")
#print(driver.get_cookies())
#sleep(2)
#driver.find_element_by_id("ls_username").send_keys("wfy")
#driver.find_element_by_id("ls_password").send_keys("111111")
#driver.find_element_by_xpath(".//*[@id='lsform']/div/div/table/tbody/tr[2]/td[3]/button").click()
#sleep(2)
#c1={'httpOnly': True, 'value': '4f3226VNioxN5BDjxB%2FSN3Uz%2FDl9yQHhpqDvCDViJZ12Zuz85f1Wwdahmdf%2ByvDQyIIYD4mk%2B0sk%2B%2BERK%2FvS', 'expiry': None, 'name': 'qGnf_2132_auth', 'path': '/', 'domain': '127.0.0.1', 'secure': False}
#driver.add_cookie(c1)
#sleep(2)
#driver.refresh()
#print(driver.get_cookie("qGnf_2132_auth"))
#print(driver.get_cookie('qGnf_2132_auth'))
#sleep(2)
#driver.delete_all_cookies()
#sleep(2)
#print(driver.get_cookies())
#sleep(2)
#driver.refresh()