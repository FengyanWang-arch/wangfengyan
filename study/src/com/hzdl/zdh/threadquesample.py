#coding=utf-8
import urllib.request
import time
hosts=["https://www.baidu.com","https://www.suning.com","https://www.jd.com",
       "https://www.vip.com/","https://uland.taobao.com"]

start=time.time()
for host in hosts:
    url=urllib.request.urlopen(host)
    print(url.read(1024))
    
print("Elapsed time:%s"%(time.time()-start))