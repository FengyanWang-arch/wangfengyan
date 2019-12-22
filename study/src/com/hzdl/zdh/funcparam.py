#coding=utf-8
def aaa(x,y):
    return x+y

def bbb(x,y):
    return x-y

def calculate(fuc,x,y):
    return fuc(x,y)

print(calculate(aaa,1,5))
print(calculate(bbb,1,6))