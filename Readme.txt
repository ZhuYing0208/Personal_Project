Author：朱莹
----------------------------------------------------------------------
操作说明：
请直接运行 tranlateContent.py 文件即可，结果会在该文件目录下得到输出文档：LocaleResource_zn_CN.properties。

文本说明：
baidu.py	翻译接口，返回翻译的结果
globe.py	定义全局变量，存储翻译后的结果，在写入文档时再获取
looop.py	实现异步编程，避免不翻译情况）
translateContent.py	读取原文件，匹配需要翻译的内容，并写入新文档中
LocaleResource_en_US.properties    输入文档	
LocaleResource_zn_CN.properties    输出文档
----------------------------------------------------------------------
感谢使用！