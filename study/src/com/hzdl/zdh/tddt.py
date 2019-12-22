#coding=utf-8
#from tlogparam import Login
from packexcl import ExcelUtil
from selenium import webdriver
from time import sleep
import ddt
import unittest

filepath=r"D:\userinfo.xlsx"
sheetName="Sheet1"
data=ExcelUtil(filepath,sheetName)
testdata=data.dict_data()
print(testdata)
@ddt.ddt
class Blog(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        url="http://127.0.0.1:81/t18bbs/forum.php"
        self.driver.get(url)
        sleep(3)
        
    def login(self,username,psw):
        self.driver.find_element_by_id("ls_username").send_keys(username)
        self.driver.find_element_by_id("ls_password").send_keys(psw)
        self.driver.find_element_by_xpath(".//*[@id='lsform']/div/div/table/tbody/tr[2]/td[3]/button").click()
        sleep(3)
        
    def is_login_success(self):
        try:
            text=self.driver.find_element_by_xpath(".//*[@id='um']/p[1]/strong/a").text
            print(text)
            return True
        except:
            return False
    @ddt.data(*testdata)  
    def test_login(self,data):
        print("当前测试数据%s"%data)
        self.login(data["username"],data["password"])
        result=self.is_login_success()
        self.assertTrue(result)
        
    def tearDown(self):
        self.driver.quit()
        
if __name__=="__main__":
    unittest.main()