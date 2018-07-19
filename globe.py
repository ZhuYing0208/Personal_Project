'''
- File name: globe.py
- Author: Zhu Ying
- Date: 07/18/2018
- Description: 定义全局变量，存储翻译后的结果，在写入文件时再获取
'''
def _init():#初始化
    global _global_dict
    _global_dict = {}

def set_value(key,value):
    """
    Description: 定义一个全局变量
    """
    _global_dict[key] = value

def get_value(key,defValue=None):
    try:
        return _global_dict[key]
    except KeyError:
        return defValue
