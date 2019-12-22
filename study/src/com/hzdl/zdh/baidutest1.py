#coding:utf-8
from selenium import webdriver
from time import sleep
from ddt import ddt,data,unpack
import texcel
import unittest

@ddt
class BaiduTest(unittest.TestCase):
    def setUp(self):
        profile_directory=r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\pwaxlqc6.default"
        profile=webdriver.FirefoxProfile(profile_directory)
        self.driver=webdriver.Firefox(profile)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.baidu.com")
        
#    def testCase_01(self):
#        driver=self.driver
#        texcel.clickButton(driver)
#        texcel.clickLogin(driver,texcel.getExcel(1,0),texcel.getExcel(1,1))
#        self.assertEqual(texcel.getText(driver),texcel.getExcel(1,2))
#        sleep(5)
#        
#    def testCase_02(self):
#        driver=self.driver
#        texcel.clickButton(driver)
#        texcel.clickLogin(driver,texcel.getExcel(2,0),texcel.getExcel(2,1))
#        self.assertEqual(texcel.getText(driver),texcel.getExcel(2,2))
#        sleep(5)
    @data(*texcel.getExcel())
    @unpack
    def testCase_03(self,username,password,expect):
        driver=self.driver
        texcel.clickButton(driver)
        texcel.clickLogin(driver,username,password)
        sleep(2)
        self.assertEqual(texcel.getText(driver),expect)
        sleep(2)
    def tearDown(self):
        self.driver.quit()
        
if __name__=="__main__":
    suite=unittest.TestLoader().loadTestsFromTestCase(BaiduTest)
    unittest.TextTestRunner(verbosity=2).run(suite)