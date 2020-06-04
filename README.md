# 自欺欺人计时器  
## 功能  
自欺欺人计时器，默认为倒计时，屏幕显示为00:01:30，屏幕上秒表每更新一次，实际时间经过1.2秒。  
可以用于体育课录1min考试视频   
## 依赖  
python 3.7.1 具体参考pygame兼容的python版本  
pygame 1.9.6 
arial字体，windows系统下默认携带  
## 安装方法  
可直接使用/dist/StupidTimer.exe，参数为默认参数  
终端下进入该文件夹执行安装   
```
pip install -r requirements.txt    
```
运行命令如下
```
python StupidTimer.py [可选参数1]  [可选参数2]
```
支持两个可选参数，第一个为显示的时间数，第二个为屏幕时钟每改变一次经过多少秒。   
参数1仅支持整数，参数2支持正小数，精度为0.01，负数会导致无限循环。如果缺少参数，则使用默认值。命令如下  
注意，参数读入为从左往右，这意味着你无法跳过参数1执行参数1
```
python StupidTimer.py
python StupidTimer.py 30 //屏幕显示为30s
python StupidTimer.py 30 1.1  //屏幕显示为30s 屏幕每经过1s 实际经过1.1s 
python StupidTimer.py 1.1 //无法使用
```  
## 现存问题  
在拖动窗口时显示时间会暂停。     
由于需要渲染时间，与实际时间会略有误差。  

## TODO  
无。没有更新计划。

## 开源协议  
本项目遵循mit开源协议

