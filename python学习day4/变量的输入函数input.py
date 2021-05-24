str = input("请输入：")
print("输入的数据为：",str)
print("输入的数据类型为：",type(str))

str = input("请输入数字：")
print("输入的数据为：",str)
print("输入的数据类型为：",type(str))  # 用户输入的任何内容 python 都认为是一个字符串

inum = int(input("请输入数字："))  # 类型转换函数：int()
print("输入的数据为：",inum)
print("输入的数据类型为：",type(inum))

fnum = float(input("请输入浮点数："))  # 类型转换函数：float()
print("输入的数据为：",fnum)
print("输入的数据类型为：",type(fnum))
