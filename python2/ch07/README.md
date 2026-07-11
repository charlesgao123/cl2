# 7.文件和数据格式化

## 7.1文件的使用
### 文件的类型
### 文件的打开和关闭
### 文件的读写

## 7.2数据组织的维度

## 7.3一维数据的处理
-f = open(curdir + 'city.txt', 'w')
+f = open(curdir + 'city.txt', 'w', encoding='utf-8')
总结： 问题出在 open() 没有指定 encoding 参数。Python 在 Windows 上默认使用系统 ANSI 代码页（中文 Windows 是 GBK），而
IDE 默认用 UTF-8 解读文件，编码不一致导致乱码。加上 encoding='utf-8' 后重新运行脚本即可解决。



## 7.4二维数据的处理

## 7.5实列解析