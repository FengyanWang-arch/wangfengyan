#coding=utf-8
import re
#text="Hi,I am Shirly Hilton."
#m=re.findall("hi",text)
#if m:
#    print(m)
#else:
#    print("not match")

#text="Hi,I am Shirly Hilton"
#m=re.findall("Hi",text)
#if m:
#    print(m)
#else:
#    print("not match")

#text="Hi,I am Shirly Hilton."
#m=re.match("hi",text)
#if m:
#    print(m)
#else:
#    print("not match")
    
#text="Hi I am Shirly Hilton."
#m=re.match("Hi",text)
#if m:
#    print(m)
#    print(m.group(0))
#else:
#    print("not match")

#text="Hi,I am Shirly Hilton."
#m=re.match(r'am',text)
#if m:
#    print(m)
#    print(m.start())
#    print(m.end())
#    print(m.group(0))
#    print(m.group(1))
#    print(m.group(2))
#    print(m.group(3))
#    print(m.group(4))
#    print(m.group(5))
#else:
#    print("not match")

#text="Hi,I am Shirly Hilton."
#m=re.match("Hi",text)
#if m:
#    print(m)
#    print(m.start())
#    print(m.end())
#else:
#    print("not match")

#text="Hi,I am Shirly Hilton."
#m=re.search("Hi",text)
#if m:
#    print(m)
#    print(m.group())
#else:
#    print("not match")

#text="Hi,I am Shirly Hilton."
#m=re.findall(r"\bHi\b",text)
#if m:
#    print(m)
#else:
#    print("not match")

#text="hi\\n"
#print(text)
#m=re.findall("hi\\\\n",text)
#if m:
#    print(m)
#else:
#    print("not match")

#text="hi\\n"
#m=re.findall(r"hi\\n",text)
#if m:
#    print(m)
#else:
#    print("not match")
    
#text="site sea sue sweet se see case sse ssee loses" 
#m=re.findall(r"\bs\w*e\b",text)
#if m:
#    print(m)
#else:
#    print("not match")
#    
#text1="my phone number is 18696626981"
#m=re.findall("1\d{10}",text1)
#if m:
#    print(m)
#else:
#    print("not match")

#text="28696744115\n285231580846\n2523158084"
#
#m=re.findall("^2\d{8}4$",text,flags=re.M)
#print(m)

#pattern=r"[0-9]{1,3}"
#string="123 1 22 678"
#match=re.findall(pattern,string,re.I)
#print(match)

#p=r"[1-9]{1,3}(\.[0-9]{1,3}){3}"
#text="127.0.0.1 192.168.1.66"
#m=re.findall(p,text)
#print(m)

#p=r"([1-9]{1,3}(\.[0-9]{1,3}){3})"
#text="127.0.0.9999 192.168.1.66"
#m=re.findall(p,text)
#for i in m:
#    print(i)

#pattern=r"1[345678]\d{9}"
#string="中奖号码为：84978981 联系电话为：13611111111"
#result=re.sub(pattern,"1xxxxxxxxxx",string,1,re.I)
#print(result)

#pattern=r"[?|&]"
#string="http://www.mingrisoft.com/login.jsp?username='mr'&pwd='mrsoft'"
#result=re.split(pattern,string,2)
#print(result)

reg="java(?:script)"
str="javascript"
m=re.findall(reg,str)
print(m)