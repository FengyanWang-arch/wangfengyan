#coding=utf-8
from selenium import webdriver
from time import sleep
from threading import Thread

def test_baidu_search(browser,url):
    driver=None
    if browser=="ie":
        driver=webdriver.Ie()
    elif browser=="firefox":
        driver=webdriver.Firefox()
    elif browser=="chrome":
        driver=webdriver.Chrome()
        
    if driver==None:
        exit()
        
    driver.get(url)
    sleep(3)
    driver.find_element_by_id("kw").send_keys("python")
    sleep(2)
    driver.find_element_by_id("su").click()
    sleep(2)
    driver.quit()
    
if __name__=="__main__":
    data={"ie":"https://www.baidu.com",
          "firefox":"https://www.baidu.com",
          "chrome":"https://www.baidu.com"}
    
    threads=[]
    for b,url in data.items():
        t=Thread(target=test_baidu_search,args=(b,url))
        threads.append(t)
        
    for thr in threads:
        thr.start()
        
    