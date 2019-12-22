#coding=utf-8
#class Employee:
#    empcount=0
#    def __init__(self,myname,mysalary):
#        self.name=myname
#        self.salary=mysalary
#        Employee.empcount+=1
#    def displaycount(self):
#        print("total employee %d"%Employee.empcount)
#    def displayemployee(self):
#        print("name:",self.name,",salary:",self.salary)
#        
#emp1=Employee("Zara",2000)
#emp2=Employee("Manni",5000)
#emp1.displayemployee()
#emp2.displayemployee()
#
#print("total employee %d"%Employee.empcount)

#class person:
#    num=0
#    def __init__(self,s):
#        self.name=s
#        person.num+=1
#    def sayhi(self):
#        print("my name is %s"%self.name)
#        
#p1=person("tom")
#p1.sayhi()
#print(p1.num)
#
#p2=person("jack")
#p2.sayhi()
#print(p2.num)

#class person:
#    __num=0
#    def __init__(self,s):
#        self.name=s
#        person.__num+=1
#    def sayhi(self):
#        print("my name is %s"%self.name)
#    def displaycount(self):
#        print("the person number is %d"%person.__num)
#        
#p1=person("tom")
#p2=person("jack")
#p1.sayhi()
#p2.sayhi()
#p2.displaycount()
#print(person.__num)
#print(p2.__num)


class Animal:
    def eat(self):
        print("eat")
    def sleep(self):
        print("sleep")
        
#class B_Animal(Animal):
#    pass
#b1=Animal()
#b2=B_Animal()
#b1.eat()
#b2.eat()
#class C_Animal(Animal):
#    def move(self):
#        print("move")
#        
#c1=C_Animal()
#c1.eat()
#c1.move()

class D_Animal(Animal):
    def eat(self):
        print("eat again")
    def move(self):
        print("move")
        
a1=Animal()
d1=D_Animal()
a1.eat()
d1.eat()
d1.move()
        