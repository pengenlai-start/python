def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of str

'''
python3 -c 'import locale;print(locale.getpreferredencoding())' 命令查看系统默认编码
bytes 包含的是由8位值所组成的序列，str 包含的是由 unicode 码点所组成的序列
我们可以编写辅助函数来确保程序收到的字符序列确实是期望要操作的类型（要知道自己想操作的到底是 Unicode 码点，还是原始的8位值。用 utf-8
标准给字符串编码，得到的就是这样的一系列8位值）
bytes 与 str 这两种实例不能在某些操作符（例如 > 、 == 、 +、 % 操作符）上面混用
从文件中读取二进制数据(或者把二进制数据写入文件)时，应该用 'rb'('wb') 这样的二进制模式打开文件
如果要从文件中读取（或者要写入文件之中）的时 unicode 数据，那么必须注意系统默认的文本编码方案。若无法肯定，可通过 encoding 参数明确指定

'''
