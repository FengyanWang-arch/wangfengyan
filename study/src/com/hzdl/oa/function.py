#coding=utf-8
def print_max(a,b):
    if a>b:
        print(a)
    else:
        print(b)
        
print_max(3,2)
print_max(6,9)

x=10
def print_x():
    x=5
    print(x)

print_x()
print(x)

#x=10
#def print_x():
#    global x
#    print(x)
#    
#print_x()
#print(x)
#
#x=10
#y=20
#def print_x():
#    global x
#    x=5
#    print(x)
#    print(y)
    
print_x()
print(x)

def say_message(message,times):
    print(message*times)
    
say_message("hello",3)
say_message("look",3)

def expection(a,b):
    print(a+b)

expection(3,2)

def favorite_game(title):
    print("my favorite game is "+title)
    
favorite_game("basketball")

#def say_message(message,times=3):
#    print(message*times)
#    
#say_message("hello")
#say_message("look")

def print_abc(a,b,c):
    print(a) 
    print(b) 
    print(c)
    
print_abc(1,2,3)

print_abc(c=3,a=1,b=2)

def maxnum(a,b):
    if a>b:
        return
    else:
        return b

print(maxnum(3,5))

c=maxnum(3,6)
print(c)

from random import randint

def compare(x,y):
    if x==y:
        print("bingo!")
        return True
    if x<y:
        print("too small!")
        return False
    if x>y:
        print("too big!")
        return False

num=50   
bingo=False
while(bingo==False):
    answer=randint(1,100)
    print(answer)
    bingo=compare(answer,num)

#from random import randint
#num=randint(1,200)
#print(num)
#
#import random
#num=random.randint(1,100)
#print(num)
#
#from random import randint as ra
#num=ra(1,100)
#print(num)

import sayhello
print(dir())