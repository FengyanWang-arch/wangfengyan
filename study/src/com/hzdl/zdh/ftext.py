#coding=utf-8
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#import re
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
#profile_directory=r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\pwaxlqc6.default"
#profile=webdriver.FirefoxProfile(profile_directory)
driver=webdriver.Firefox()
driver.get("http://127.0.0.1:81/t18bbs/forum.php")
driver.delete_all_cookies()
driver.refresh()
driver.find_element_by_id("ls_username").send_keys("wfy")
driver.find_element_by_id("ls_password").send_keys("111111")
#driver.find_element_by_xpath(".//*[@id='lsform']/div/div/table/tbody/tr[2]/td[3]/button").click()
WebDriverWait(driver,20).until(lambda x:x.find_element_by_xpath(".//*[@id='lsform']/div/div/table/tbody/tr[2]/td[3]/button")).click()
#sleep(3)
WebDriverWait(driver,30).until(lambda y:y.find_element_by_xpath(".//*[@id='category_1']/table/tbody/tr[1]/td[2]/h2/a")).click()
#driver.find_element_by_xpath(".//*[@id='category_1']/table/tbody/tr[1]/td[2]/h2/a").click()
sleep(3)
driver.find_element_by_xpath(".//*[@id='newspecial']/img").click()
sleep(3)
#page=driver.page_source
#print(page)
#url_list=re.findall('href=\"(.*?)\"',page,re.S)
#url_all=[]
#for url in url_list:
#    if 'http' in url:
#        print(url)
#        url_all.append(url)
#print(url_all)     
#sleep(3)
etitle=r"Selenium2+python 自动化-富文本"
ebody=r"这里是发帖的正文,快乐每一天。好好学习"
driver.find_element_by_id("subject").send_keys(etitle)
sleep(3)
#iframe = driver.find_elements_by_tag_name('iframe')[0]
#print(iframe)
#sleep(2)
#driver.switch_to.frame("e_iframe")
#sleep(3)
#driver.find_element_by_xpath("html/body").send_keys(Keys.TAB)
#driver.find_element_by_xpath("html/body").send_keys(ebody)
#sleep(2)
#driver.switch_to_default_content()

js='document.getElementById("e_iframe")' \
'.contentWindow.document.body.innerHTML="%s"' % ebody
driver.execute_script(js)
#driver.find_element_by_id("e_attach").click()
#driver.switch_to_alert()
#driver.find_element_by_id("attachnew_1").send_keys(r"C:\11.jpeg")
#driver.find_element_by_xpath(".//*[@id='uploadbtn']/button").click()
#driver.find_element_by_id("attach_confirms").click()
#sleep(2)
#js="var q=document.documentElement.scrollTop=10000"
#driver.execute_script(js)
#sleep(3)
#js="var q=document.documentElement.scrollTop=0"
#driver.execute_script(js)
#def scroll_foot():
#    if driver.name=="chrome":
#        js="var q=document.body.scrollTop=10000"
#    else:
#        js="var q=document.documentElement.scrollTop=10000"
#    driver.execute_script(js)
#
#def scroll_top():
#    if driver.name=="chrome":
#        js="var q=document.body.scrollTop=0"
#    else:
#        js="var q=document.documentElement.scrollTop=0"
#    driver.execute_script(js)
#
#scroll_foot()
#sleep(2)
#scroll_top()
#sleep(2)
#
js="window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)
sleep(3)
js="window.scrollTo(0,0)"
driver.execute_script(js)
sleep(3)
#sub=driver.find_element_by_id("postsubmit")
#driver.execute_script("arguments[0].scrollIntoView();",sub)
#sub.click()

