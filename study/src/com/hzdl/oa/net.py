#coding=utf-8
import requests
#r=requests.get(url="https://cn.bing.com/images/search?view=detailV2&ccid=xPpy2xAh&id=F9490EDD01C773AD56A18ABED2A575D6A84F4D13&thid=OIP.xPpy2xAhSyktO8_RKvpQuAHaLE&mediaurl=http%3a%2f%2fimage.tupian114.com%2f20100908%2f04040876.jpg&exph=798&expw=534&q=%e7%8e%8b%e7%8f%9e%e4%b8%b9%e5%86%99%e7%9c%9f&simid=607986305264058509&selectedIndex=3&ajaxhist=0")
#file=open("C:\\baidu.jpg","wb")
#file.write(r.content)
#file.close()

#r=requests.get(url="http://www.weather.com.cn/data/sk/101040100.html")
#r=requests.get(url="http://dict.baidu.com/s",params={'wd':'python'})
#r.encoding='utf-8'
#print(r.status_code)
#print(r.text)
import json
r=requests.get(url='http://www.weather.com.cn/data/sk/101040100.html')
r.encoding='utf-8'
data=json.loads(r.text)
city=data["weatherinfo"]["city"]
sd=data["weatherinfo"]["SD"]
wd=data["weatherinfo"]["WD"]
ws=data["weatherinfo"]["WS"]
ap=data["weatherinfo"]["AP"]
print("城市：%s\n温度：%s\n风向：%s\n风力：%s\n湿度：%s\n"%(city,sd,wd,ws,ap))

