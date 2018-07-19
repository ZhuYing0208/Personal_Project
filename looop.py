'''
- File name: looop.py
- Author: Zhu Ying
- Date: 07/18/2018
- Description: 实现异步处理，避免翻译时出现不翻的情况
'''
import baidu
import asyncio
import globe
globe._init()
def transalteEnToZh(content):
    """ 
    Description: 调用翻译
    """
    r = yield from asyncio.sleep(1)
    globe.set_value('contentCh',baidu.baidu_translate(content))

def runEventLoop(content):
    """ 
    Description: 实现循环复用
    """
    loop = asyncio.new_event_loop()
    loop.run_until_complete(transalteEnToZh(content))
    loop.close()
