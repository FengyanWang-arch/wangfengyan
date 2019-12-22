#coding=utf-8
from selenium import webdriver

def browser(browser="forefox"):
    try:
        if browser=='forefox':
            driver=webdriver.Firefox()
            return driver
        elif browser=="chrome":
            driver=webdriver.Chrome()
            return driver
        elif browser=="ie":
            driver=webdriver.Ie()
            return driver
        elif browser=="phantomjs":
            driver=webdriver.PhantomJS()
            return driver
        else:
            print("Not found browser!")
    except Exception as msg:
        print("open browser error:%s"%msg)
        
if __name__=="__main__":
    driver1=browser()
    driver1.get("https://www.baidu.com")
    print("open browser:%s"%driver1.name)
    print(driver1.title)
    
    driver2=browser("chrome")        
    driver2.get("http://127.0.0.1:81/t18bbs/forum.php")
    print("open browser:%s"%driver2.name)
    print(driver2.title)
        
        