# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
# �ȴ�ʱ�� 10 �룬Ĭ�� 0.5 ��ѯ��һ��
WebDriverWait(driver, 10).until(lambda x:
x.find_element_by_id("kw")).send_keys("yoyo")
# �ж� id Ϊ kw Ԫ���Ƿ���ʧ
#is_disappeared = WebDriverWait(driver, 10, 1).\
#until_not(lambda x: x.find_element_by_id("kw").is_displayed())
#print("is_disappeared")