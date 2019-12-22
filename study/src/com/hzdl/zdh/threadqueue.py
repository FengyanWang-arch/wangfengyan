#!/usr/bin/env python
import queue
import threading
import urllib.request
import time

hosts=["https://www.baidu.com","https://www.suning.com","https://www.jd.com",
       "https://www.vip.com/","https://uland.taobao.com"]

queue=queue.Queue()

class ThreadUrl(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue=queue
        
    def run(self):
        while True:
            host=self.queue.get()
            url=urllib.request.urlopen(host)
            print(url.read(1024))
            self.queue.task_done()
            
start=time.time()
def main():
    for i in range(5):
        t=ThreadUrl(queue)
        t.setDaemon(True)
        t.start()
        
        for host in hosts:
            queue.put(host)
            
        queue.join()

main()
print("Elapsed time:%s"%(time.time()-start))     