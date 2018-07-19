'''
- File name: baidu.py
- Author: Zhu Ying
- Date: 07/10/2018
- Description: 实现调用百度翻译API进行语音识别后的内容翻译
- Function List:
  baidu_translate: 包含机器翻译输入、发送、返回和输出的整个过程
'''
import http.client  
import hashlib  
import json  
import urllib  
import random

def baidu_translate(content):
    '''
    description: 调用百度翻译API
    '''
    appid = '20151113000005349'  
    secretKey = 'osubCEzlGjzvw8qdQc41'  
    httpClient = None  
    myurl = '/api/trans/vip/translate'  
    q = content  
    fromLang = 'en' # 源语言
    toLang = 'zh'   # 翻译后的语言
    salt = random.randint(32768, 65536)  
    sign = appid + q + str(salt) + secretKey  
    sign = hashlib.md5(sign.encode()).hexdigest()  
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(  
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(  
        salt) + '&sign=' + sign  
  
    try:  
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')  
        httpClient.request('GET', myurl)  
        # response是HTTPResponse对象  
        response = httpClient.getresponse()  
        jsonResponse = response.read().decode("utf-8")# 获得返回的结果，结果为json格式  
        js = json.loads(jsonResponse)  # 将json格式的结果转换字典结构  
        dst = str(js["trans_result"][0]["dst"])  # 取得翻译后的文本结果
       # print(dst,end='') # 打印结果
        return dst
    except Exception as e:  
        print(e)  
    finally:  
        if httpClient:  
            httpClient.close()  

