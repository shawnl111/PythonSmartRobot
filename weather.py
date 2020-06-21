import requests, json
url = 'http://t.weather.sojson.com/api/weather/city/'

def inquire():
    city = input("请输入你要查询的城市：\n\t\t\t\t\t\t")
    print("正在为您查询...")
    with open("city.json",'rb') as f:
        cities = json.load(f)
    city = cities.get(city)#通过城市的中文获取城市代码
    response = requests.get(url + city)#网络请求，传入请求api+城市代码
    d = response.json()#将数据以json形式返回，这个d就是返回的json数据
    if(d['status'] == 200):#当返回状态码为200，输出天气状况
        print("城市：", d["cityInfo"]["parent"], d["cityInfo"]["city"])
        print("时间：", d["time"], d["data"]["forecast"][0]["week"])
        print("温度：", d["data"]["forecast"][0]["high"], d["data"]["forecast"][0]["low"])
        print("天气：", d["data"]["forecast"][0]["type"])