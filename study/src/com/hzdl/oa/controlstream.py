#coding=utf-8
#for letter in "python":
#    if letter=='h':
#        break
#    print("current letter:",letter)
#        
        
#for letter in "python":
#    if letter=='h':
#        continue
#    print("current letter:",letter)

#for i in range(1,10):
#    print(i)


#for i in range(1,10):
#    for j in range(1,i+1):
#        print("%d*%d=%-4d"%(j,i,i*j),end='')
#    print()

#for i in range(1,6):
#    print("*")

#for i in range(1,6):
#    print("*",end=' ')

#for i in range(1,6):
#    for j in range(1,i+1):
#        print('*',end=' ')
#    print()

#for i in range(1,10):
#    for j in range(1,i+1):
#        print("%d*%d=%-4d"%(j,i,i*j),end=' ')
#    print()

#abc=10
#num=input("please enter a number:\n")
#if abc==int(num):
#    print("right!")
#else:
#    print("wrong!")

#abc=10
#num=int(input("please enter a number:\n"))
#if abc>num:
#    print("too small!")
#if abc<num:
#    print("too big!")
#if abc==num:
#    print("right!")

#abc=10
#num=int(input("please enter a number:\n"))
#if abc==num:
#    print("right!")
#elif abc>num:
#    print("too small!")
#else:
#    print("too big!")


#num=int(input("please enter a number:\n"))
#if num>=0:
#    if num<=20:
#        print("[0,20]")
#    else:
#        print(">20")
#else:
#    if num>-10:
#        print("(-10,0)")
#    else:
#        print("<=-10")

abc=50
marks=True
n=0
while marks:
    n+=1
    num=int(input("please enter a number:\n"))
    if num==abc:
        print("right!")
        marks=False
    if num>abc:
        print("too big!")
        if n==5:
            print("too stupid")
    if num<abc:
        print("too small!")
        if n==5:
            print("too stupid")
        
    