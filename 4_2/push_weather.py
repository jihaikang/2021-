import requests
import json
 
webhook = 'https://qmsg.zendee.cn/send/9b55030bd2e4a2cdd54d066bc2d02e49'   # Qmsg酱接口
api_url = 'https://tianqiapi.com/api'               # 免费天气接口
push_wx = 'http://pushplus.hxtrip.com/send/4318aa128ac24bd1937092160fa68fd6' # 不知为何Push推送不能够接受这种json格式，还是我自己不会设计json格式
city = '景德镇'
 
 
 
weatherParams = {
    'appid': '58191412',            # 必填，也可以填自己注册的
    'appsecret': 'F3yGBa4u ',    # 必填，也可以填自己注册的
    'version': 'v6',                    # 必填
    'city': city,                       # 城市代码，名字，ip三选一，默认ip
}
 
def main_handler(url, params):
    dataList = []                   # 创建空列表
    res = json.loads(requests.get(url, params).text)       # 提交post
    city = res['city']              # 城市名字
    date = res['date']              # 当前日期
    week = res['week']              # 当前星期
    update = res['update_time']     # 更新时间
    wea = res['wea']                # 天气情况
    tem = res['tem']                # 实时温度
    tem1 = res['tem1']              # 温度上限
    tem2 = res['tem2']              # 温度下限
    hunidity = res['humidity']      # 湿度
    win = res['win']                # 风向
    win_speed = res['win_speed']    # 风力等级
    visibility = res['visibility']  # 能见度
    air = res['air']                # 空气质量
    air_level = res['air_level']    # 空气质量等级
    air_tips = res['air_tips']      # 空气质量描述
 
    dataList.extend(
        [city, date, week, update, wea, tem, tem1, tem2, hunidity, win, win_speed, visibility, air, air_level,
         air_tips])                 # 向空列表中追加天气内容
    QQPusher(dataList)
    wxpush(dataList)
 
 
def QQPusher(dataList):
    data = {
        'msg': '今日天气推送&#127808; \n---\n城市:{}\n日期:{}\n星期:{}\n更新日期:{}\n---\n天气情况:{}\n 实时温度:{}℃, 温度范围:{}/{}℃\n湿度:{}\n---\n风向{}\n风力等级:{}\n能见度:{}\n---\n空气质量:{}\n空气质量等级:{}\n空气质量描述：{}\n温馨提示：疫情期间，外出请佩戴口罩！'.format(
            dataList[0], dataList[1], dataList[2], dataList[3], dataList[4], dataList[5], dataList[6], dataList[7],
            dataList[8], dataList[9], dataList[10], dataList[11], dataList[12], dataList[13], dataList[14])
    }
    requests.post(webhook, data)
def wxpush(datalist):
    data = {
        'msg': '今日天气推送&#127808; \n---\n城市:{}\n日期:{}\n星期:{}\n更新日期:{}\n---\n天气情况:{}\n 实时温度:{}℃, 温度范围:{}/{}℃\n湿度:{}\n---\n风向{}\n风力等级:{}\n能见度:{}\n---\n空气质量:{}\n空气质量等级:{}\n空气质量描述：{}\n温馨提示：疫情期间，外出请佩戴口罩！'.format(
            dataList[0], dataList[1], dataList[2], dataList[3], dataList[4], dataList[5], dataList[6], dataList[7],
            dataList[8], dataList[9], dataList[10], dataList[11], dataList[12], dataList[13], dataList[14])
    }
    requests.post(push_wx,data)
 
main_handler(api_url, weatherParams)
