#coding=utf-8
#filewrite=open("111.txt","w")
#filewrite.write("i like python")
#filewrite.close()
#
#fileopen=open("111.txt")
#data=fileopen.read()
#print(data)

#try:
#    print("please enter a number:")
#    num=int(input())
#    if num>0:
#        print("yes")
#    else:
#        print("no")
#except:
#    print("fialed")
#    print("you must enter a number.")

#try:
#    n=5*6
#    print("n=",n)
#    m=6/0
#    print("m=",m)
#except ZeroDivisionError:
#    print("发生0做为除数的异常")
#print("计算完成")

#try:
#    f=open("abc.txt")
#    data=f.read()
#    print(data)
#    f.close()
#except (IOError,TypeError,ValueError):
#    print("this file is not exist!")

#try:
#    f=open("abc.txt")
#    data=f.read()
#    print(data)
#    f.close()
#except IOError:
#    print("this file is not exist!")
#except TypeError:
#    print("Type is wrong!")
#except ValueError:
#    print("Value is wrong!")    

#try:
#    print("hello world")
#except:
#    print("fail")
#else:
#    print("there is no exception")

try:
    print("please enter a number")
    num=int(input())
    if num<0:
        raise Exception
except:
    print("this number is <0")
else:
    print("this number is >=0")
finally:
    print("bye")