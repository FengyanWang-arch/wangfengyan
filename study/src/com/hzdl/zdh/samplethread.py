import _thread
from time import sleep,ctime

def loop0():
    print("loop 0 start time:",ctime())
    sleep(4)
    print("loop 0 end time:",ctime())
    
def loop1():
    print("loop1 start time:",ctime())
    sleep(2)
    print("loop1 end time:",ctime())
    
def main():
    print("program start time:",ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1,())
    sleep(6)
    print("program end time:",ctime())
    
if __name__=="__main__":
    main()