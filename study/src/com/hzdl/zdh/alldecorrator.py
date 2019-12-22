#coding=utf-8
def test_result(func):
    def inner(*args,**kwargs):
        try:
            func(*args,**kwargs)
            print("程序未抛异常：pass")
        except:
            print("程序抛异常：fail")
        return func(*args,**kwargs)
    return inner

@test_result
def ccc(a,b):
    return a+b

print(ccc(1,3))
print(ccc(1,2,3))