#coding:utf-8
import xlrd
from selenium import webdriver
import time as t
def getExcel(file_name="D:\\test.xlsx"):
#def getExcel(rowValue,colValue,file_name="D:\\test.xlsx"):
    rows=[]
    book=xlrd.open_workbook(file_name)
    sheet=book.sheet_by_index(0)
    for row in range(1,sheet.nrows):
        rows.append(list(sheet.row_values(row,0,sheet.ncols)))
    return rows
#    return sheet.cell_value(rowValue,colValue)

def clickButton(driver):
    driver.find_element_by_link_text('登录').click()
    t.sleep(2)
    
def clickLogin(driver,username,password):
    name=driver.find_element_by_id('TANGRAM__PSP_10__userName')
    name.clear()
    name.send_keys(username)
    t.sleep(2)
    passwd=driver.find_element_by_id('TANGRAM__PSP_10__password')
    passwd.clear()
    passwd.send_keys(password)
    t.sleep(2)
    driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
    t.sleep(2)
    
def getText(driver):
    return driver.find_element_by_id('TANGRAM__PSP_10__error').text
    

    

if __name__=='__main__':
    print(getExcel())