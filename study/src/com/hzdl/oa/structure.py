#coding=utf-8
#list1=["physics","chemistry",1997,2000];
#list2=[1,2,3,4,5,6,7];
#print(list1[0])
#print(list2[0:7])
#print(list2[6])
#print(list2[2])
#list2[2]=2001
#print(list2[0:7])

#l1=[1,2,3,4,5]
#l2=[1,"a",2,"b",l1]
#print(l1)
#print(l2)

#l6=[1,"a",["pysics","chemistry",1997,2000],6,"c"]
#print(l6)
#print(l6[2])
#print(l6[4])

#tup1=("physics","chemistry",1997,2000)
#tup2=(1,2,3,4,5)
#tup3="a","b","c","d","e"

#print(tup1[0])
#print(tup2[1:5])
#print(tup3)

#tup1=(12,34.56)
#tup2=("abc","xyz")
#tup3=tup1+tup2
#print(tup1) 
#print(tup2)
#print(tup3)

#t1=()
#t2=(1)
#t3=(1,)
#print(t1)
#print(t2)
#print(t3)
#print(dir())

#dict={'name':'zara','age':18,'class':'first'}
#
#print(dict["age"])
#dict['school']='dps school'
#print(dict)
#print("dict['school']:",dict['school'])

l1=[1,2,3,4,5]
t1=(1,2,3,4,5)
d1={'a':1,'b':2,'c':3}
#
#print(l1[2])
#print(t1[2])
#print(d1['b'])
#print(l1[-1])
#print(l1[-2])
#print(t1[-5:])
#print(t1[-2])

#for i in l1:
#    print(i)
#    
#for j in t1:
#    print(j)
#    
#for m in d1:
#    print(d1[m])
    
#l1.append(6)
#d1['d']=6
#print(l1)
#print(d1)
#t1.append(6)

#del l1[3]
#del d1['b']
#print(l1)
#print(d1)
#del t1[3]
#print(t1)

#str1="my name is tom"
#l2=str1.split()
#print(l2)
#print(l2[2])
#s1=" "
#print(s1.join(l2))
#s2="."
#print(s2.join(l2))

str1="my name is tom"
for i in str1:
    print(i,end=' ')
    
print(str1[4])
print(str1[6])
print(str1[3:-2])
print(str1[0:-2])