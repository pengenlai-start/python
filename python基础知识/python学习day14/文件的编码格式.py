'''
文件的编码格式
    python2.x       ASCII 一个字节
    python3.x       UTF-8 1~6个字节

    大多数汉字会使用3个字节表示
在 python2.x 中使用中文
    # *-* coding:utf-8 *-*   或者  # coding = utf-8

eg.  hello_str = u 'hello 世界'  告诉解释器这是一个 utf-8 编码格式的字符串，否则遍历该字符串会出问题
                                仍以字节为单位遍历字符串
'''