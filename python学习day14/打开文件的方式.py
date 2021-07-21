"""
打开文件的方式
语法
file = open("文件名","访问方式")

访问方式
r       只读，文件指针在文件开头
w       只写，存在，覆盖; 不存在，新建
a       追加，存在，在末尾追加; 不存在，新建
r+      读写，不存在，异常
w+      读写, 存在，覆盖; 不存在，新建
a+      读写，存在，追加; 不存在, 新建

readline   ------ 按行读取

eg.

file = open("文件名")
while True:
    text = file.read()
    if not text:
        break
    print(text, end="")  # text 读取的内容中包含 '\n'
file.close()
"""