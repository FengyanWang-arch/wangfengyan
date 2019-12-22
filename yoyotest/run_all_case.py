#coding=utf-8
import unittest
import HTMLTestRunner
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os
def add_case(case_path,rule):
#    case_dir="D:\jiaoben2\python\yoyotest\src\case"

    testcase=unittest.TestSuite()

    discover=unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)

    for test_suite in discover:
        for test_case in test_suite:
            testcase.addTests(test_case)
    print(testcase)
    return testcase

def run_case(all_case,report_path):
    now=time.strftime("%Y_%m_%d_%H_%M_%S")
    report_abspath=os.path.join(report_path,now+"result.html")
    fp=open(report_abspath,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="自动化测试报告，测试结果如下：",description="用例执行情况：")
    runner.run(all_case)
    fp.close()

def get_report_file(report_path):
    lists=os.listdir(report_path)
    lists.sort(key=lambda fn:os.path.getmtime(os.path.join(report_path,fn)))
    print("最新测试生成的报告："+lists[-1])
    report_file=os.path.join(report_path,lists[-1])
    return(report_file)

def send_mail(sender,psw,receiver,smtpserver,report_file):
    with open(report_file,"rb") as f:
        mail_body=f.read()
    msg=MIMEMultipart()
    body=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg['Subject']="自动化测试报告"
    msg["from"]=sender
    msg["to"]=psw
    msg["date"]=time.strftime("%a,%d%b%Y%H%M%S%z")
    msg.attach(body)
    att=MIMEText(open(report_file,"rb").read(),"base64","utf-8")
    att["Content-Type"]="application/octet-stream"
    att["Content-Disposition"]='attachment;filename="report.html"'
    msg.attach(att)
    smtp=smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(sender,psw)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
    print("test report email has send out!")
if __name__=="__main__":
#    runner=unittest.TextTestRunner()
#    runner.run(all_case())
    case_path="D:\jiaoben2\python\yoyotest\src\case"
    rule="test*.py"
    all_case=add_case(case_path,rule)
    report_path=r"D:\jiaoben2\python\yoyotest\report"
    run_case(all_case,report_path)
    report_file=get_report_file(report_path)
    sender="1453025309@qq.com"
    psw="qmbhesxgyurqgiha"
    receiver="1453025309@qq.com"
    smtp_server="smtp.qq.com"
    send_mail(sender,psw,receiver,smtp_server,report_file)
    
#    fp = open(report_path, "wb")
    
#    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='这是我的自动化测试报告',description='用例执行情况：')
#    
#    runner.run(all_case())
#    fp.close()