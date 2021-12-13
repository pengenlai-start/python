'''
Tuple 元组 () ，元组的元素不能修改，可保存不同类型的数据
元组中只包含一个元素时，需要在元素后面添加逗号
'''

tup = (1)   # 数字
print("type = %s" % type(tup))

tup = (1,)  # 单元素元组
print("type = %s" % type(tup))

tup = ()  # 空元组
print("type = %s" % type(tup))

tup = (1, 2, 5)
cnt = tup.count(2)  # 获取数据的出现次数
print("cnt = %d" % cnt)
index = tup.index(5)  # 获取数据第一次出现的索引
print("index = %d" % index)

print("%s %d" % ("pel", 18))  # 格式字符串
info = ('pel', 28)
info_str = "%s 年龄 %d" % info
print(info_str)

'''
元组的一般应用场景：
    1） 函数的参数和返回值
    2） 格式字符串
    3） 让列表不可以被修改
    
元组和列表之间的转换：
    tuple(列表)
    list(元组)
'''
