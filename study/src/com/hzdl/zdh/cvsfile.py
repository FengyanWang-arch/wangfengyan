#!/usr/bin/env python
#coding:utf-8
import csv

def getCsv(file_name='d:/test.csv'):
    rows=[]
    with open(file_name,'r') as f:
        readers=csv.reader(f,delimiter=',',quotechar='|')
        next(readers,None)
    
        for row in readers:
            rows.append(row)
        return rows  #返回列表
    
#def writeCsv(file_name='d:/test.csv'):
#    with open(file_name,'w') as f:
#        write=csv.writer(f)
#        write.writerow(['Element','system'])
#        data=[['selenium','webdriver'],['appium','android'],['appium','ios'],['selenium','python']]
#        write.writerows(data)
        
#    f.close()
    
if __name__=='__main__':
#        writeCsv()
        print(getCsv()) #获取列表
