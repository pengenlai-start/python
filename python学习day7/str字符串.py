# 字符串 -- 一对单引号或双引号定义      \" ----双引号      \' ----- 单引号
# 如果字符串内部需要使用 " ，使用单引号定义字符串
# 如果字符串内部需要使用　',可以使用双引号定义字符串

'''
len(字符串)    字符串长度
字符串.count(字符串１)　    字符串１在字符串中出现的次数
字符串[index]  取值
字符串.index(字符串１)     字符串１在字符串中第一次出现的索引
'''

def len_str(str, char, index):
    '''测试字符串长度函数'''
    print("len = %d" % len(str))
    print("str[%d] = %s" % (index, str[index]))
    print("str.index(%s) = %d" % (char, str.index(char)))


len_str("hello world", "wo", 6)

'''
string.isspace()    判断字符串中是否只由空白字符组成

判断字符串中是否只包含数字　——　均不能判断小数
string.isdecimal() ——　1、２ 
string.isdigit() —— 1、２、　\u00b2
string.isnumeric() ——　1、２、 \u00b2、　一千零一
'''
str = '12345'
space = '\n\t'
s1 = '12\u00b2'
s2 = '一千零一'

print(str.isdecimal())
print(space.isspace())
print(s1.isdigit())
print(s2.isnumeric())

'''
string.starstwith(str)  是否以 str 开头
string.endswith(str)  是否以　str 结尾
string.find(str, start = 0, end = len(string))  str　是否在指定范围内，返回索引值，否则返回　-1
string.replace(old_str, new_str, num = string.count(old))   替换，且替换次数不超过　num ,replace 不改变原字符串，返回新字符串
string.ljust(width) 左对齐
string.rjust(width) 右对齐
string.center(width) 居中对齐   width 为长度
string.lstrip() 去除　string 左边的空白字符
string.rstrip() 去除 string 右边的空白字符
string.strip() 去除　string 左右两边的空白字符
string.split(str="", num)   以 str 为分隔符将字符串拆分为　num + 1 个子字符串，str　默认包含所有空白字符
string.join(seq)    seq－－－序列:列表　元组　字典   以　string 为分隔符将　seq　中所有的元素合并为一个新字符串
'''