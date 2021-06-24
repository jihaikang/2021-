from aip import AipOcr
import json
# 首先安装百度 Python SDK pip install baidu-aip
""" 你的 APPID AK SK """
APP_ID = '19623638'
API_KEY = 'BFhQK7FhV26MM7YGorNHCcpv'
SECRET_KEY = 'hfVol8fPaZSYinU7PBi0R7CzGKGAQ6F7'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    """ 读取图片 """
    with open(filePath, 'rb') as fp:
        return fp.read()

""" 调用通用文字识别, 图片参数为本地图片 """
result = client.basicGeneral(get_file_content('1话 1.jpg'))
print(json.dumps(result, ensure_ascii=False, indent=2))