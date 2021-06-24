import requests as r
import time
import json
# 导入相关库
 # 调用别人的接口 https://www.sapi.run/hero/select.php?hero=%s&type=%s
while True:  # 建立死循环，否则查询一次后会退出程序
    hero = input("输入需要查询的英雄:")  # 输入查询的英雄
    if hero == "":  # 判断输入的字符串是否是空的
        print("您输入无效")
    type = input("输入需要的大区是qq还是wx，请直接输入qq或wx:")
    if type != "qq" and type != "wx":  # 查询大区只有qq和wx
        print("您输入的大区无效")
    else:
        source = r.get("https://www.sapi.run/hero/select.php?hero=%s&type=%s" % (hero, type)).text
        # get获取，hero英雄，type为qq或wx
        _json = json.loads(source)
        # 返回json格式，转换为字典
        if _json["code"] == "200":
            # code为200，表示返回正常，其余数值则错误
            title = _json["data"]["heroName"]  # 英雄名称
            print("英雄:%s" % title)
            area = _json["data"]["area"]  # 区名称
            areaPower = _json["data"]["areaPower"]  # 区最低战力
            areaTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(_json["data"]["areaTime"])))
            # 更新时间是时间戳，这里将时间戳转到时间文本
            print("县/区:%s(%s) %s" % (area, areaPower, areaTime))
            city = _json["data"]["city"]
            cityPower = _json["data"]["cityPower"]
            cityTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(_json["data"]["cityTime"])))
            print("市:%s(%s) %s" % (city, cityPower, cityTime))
            province = _json["data"]["province"]
            provincePower = _json["data"]["provincePower"]
            provinceTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(_json["data"]["provinceTime"])))
            print("省:%s(%s) %s" % (province, provincePower, provinceTime))
        else:
            print("错误代码：%s %s" % (_json["code"], _json["msg"]))
        print("\n")