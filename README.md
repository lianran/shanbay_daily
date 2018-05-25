# 扇贝每日单词-->打印

本脚本用于获取扇贝每次单词，并按照”序号“-”单词“-”音标“-”中文“的格式存储到excel文件中。

本脚本根据[shanbay_daily](https://github.com/cijianzy/shanbay_daily)项目改写。

#### 脚本运行环境

* python 2.7

#### 使用方式

##### 运行前准备

1. 运行脚本前，需要打开扇贝，进入单词背诵页面，并点击查看"我的词库"->"每日单词"，查看单词的页数；
2. 使用chrome获取自己的userid，并填入到configuration.sjon文件中
	
		{
		  "user_id": "1526997028684", #用户id
		  "daily_page_num": 20 #页数单词
		}
		
 ###### 关于userid的获取方式
 
 使用chrome打开每日单词页面，右键 -> “Inspect" -> "Network"，然后刷新页面获得，并在下面console中找到如下请求，后面即为user_id。
 	
 		page=1&_=1527233553516


 		
##### 脚本运行

1. 运行 

		python shanbay_getdaily.py
	
	获取数据到 ./data文件加下，并附带相关音频
	
2. 运行 

		python ToExcel.py 
		
	得到 'my words.xls'文件，包含单词读音和解释。
	