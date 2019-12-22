#coding=utf-8
import pymysql
import random
#conn=pymysql.Connect(host="localhost",user="root",passwd="root",db="t18bbs",port=3306)
##connect(host="localhost",user="root",passwd="root",db="t18bbs",port="3306")
#cur=conn.cursor()
#count=cur.execute("select * from users")
#print(count)
#result=cur.fetchone()
#print("id:%s name:%s age:%s sex:%s"%result)
#
#cur.close()
#conn.close()

conn=pymysql.Connect(host="localhost",user="root",passwd="root",db="t18bbs",port=3306)
cur=conn.cursor()
cur.execute("delete from users")
cur.execute("insert into users values(%s,%s,%s,%s)",(1,"zhangsan1",26,'男'))
cur.execute("insert into users values(%s,%s,%s,%s)",(2,"zhangsan2",28,"女"))

sql_l=[]
for i in range(3,11):
    sql_l.append([i,'zhangsan'+str(i),random.randint(20,30),"男"])
    
cur.executemany("insert into users values(%s,%s,%s,%s)",sql_l)

count=cur.execute("select * from users")
print(count)

result=cur.fetchone()
print("id:%d,name:%s,age:%d,sex:%s"%result)

result1=cur.fetchmany(5)
#print(result1)
for re1 in result1:
    print("id:%d name:%s age:%d sex:%s"%re1)
    
result2=cur.fetchall()
for re2 in result2:
    print("id:%d name:%s age:%d sex:%s"%re2)
    
conn.commit()
cur.close()
conn.close()

