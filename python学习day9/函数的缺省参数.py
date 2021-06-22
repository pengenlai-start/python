# 函数的缺省参数　——　某个参数指定一个默认值，具有默认值的参数就叫做缺省参数
"""
指定函数的缺省参数 --- 必须保证带有默认值的缺省参数在参数列表的末尾
eg
def print_info(name, gender = True):
    gender_text = "男"
    if not gender:
        gender_text = "女"
    print("%s 是　%s " % (name,gender_text))

eg
def print_info(gender = True, name)   错误

调用函数时，如果有多个缺省参数，需要指定参数名
"""
