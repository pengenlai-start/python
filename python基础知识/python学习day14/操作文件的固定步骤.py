"""
操作文件的固定步骤
1、打开文件 ----> 文件名区分大小写
2、读、写文件  ---> 读， 将文件内容读入内存; 写， 将内存内容写入文件
3、关闭文件

eg.

file = open("文件名")
text = file.read()
print(text)
file.close()

"""