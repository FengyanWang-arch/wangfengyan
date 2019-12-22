#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support  import expected_conditions as EC

driver=webdriver.Firefox()
url="https://www.baidu.com"
driver.get(url)
locator=("name","tj_trnews")
text="新闻"
result=EC.text_to_be_present_in_element(locator,text)(driver)
print(result)

text1="新闻网"
result1=EC.text_to_be_present_in_element(locator,text1)(driver)
print(result1)

locator2=("id","su")
text2="百度一下"
result2=EC.text_to_be_present_in_element_value(locator2,text2)(driver)
print(result2)