'''
- File name: translateContent.py
- Author: Zhu Ying
- Date: 07/18/2018
- Description: 读取原文件，并进行翻译内容匹配，写入新文件中
'''
import baidu
import asyncio
import looop
import  re
import  globe

def transContent(filePath,outFilePath):
    '''
    description: 读取写入文件，用正则表达式匹配需要翻译的内容
    '''
    allData=[]
    result=[]
    propKey=''
    contentCh=''
    with open(outFilePath,'w') as outFile:
        #读取文件
        with   open(filePath,'r') as f:
            #写入文件
            for line in f:
                #开始匹配
                if re.match(r'#.*.*',line,re.M|re.I) is None and line!='\n':
                    propKey=line.split('=',1)[0].strip();
                    print(propKey)
                    contentEng=line.split('=',1)[1].strip()
                    if re.match( '(.*).(.htm|.gif)', contentEng, re.I):
                        contentCh=contentEng
                    else:
                        matchGroup=re.match(r'(.*?)<[a-zA-Z].*>(.*)</[a-zA-Z]>(.*).*', contentEng, re.M|re.I)
                        if matchGroup:
                            looop.runEventLoop(matchGroup.group(1))
                            tempHead=globe.get_value('contentCh') if globe.get_value('contentCh') is not None else ''
                            forward=tempHead+re.findall('<.*>',contentEng)[0]
                            looop.runEventLoop(matchGroup.group(3))
                            tempRear=globe.get_value('contentCh') if globe.get_value('contentCh') is not None else ''
                            contentCh=forward+tempRear
                        else:
                            looop.runEventLoop(contentEng)
                            contentCh=globe.get_value('contentCh') if globe.get_value('contentCh') is not None else ''
                    outFile.write(propKey +'='+ contentCh + '\n')
                else:
                    outFile.write(line.strip())
                    
        outFile.close()

if __name__ == '__main__':    
	filePath = 'LocaleResource_en_US.properties'
	outFilePath='LocaleResource_zn_CN.properties'
	transContent(filePath,outFilePath)
	print('success...')

