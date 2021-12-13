"""
异常

捕获异常的语法格式

try:
    尝试执行的代码
except:
    出现错误的处理
    ...

错误类型捕获

try:
    尝试执行的代码
except 错误类型1:
    针对错误类型1的错误处理
except 错误类型２:
    针对错误类型２的错误处理
except Exception as result:  # 捕获未知错误
    print("未知错误　%s " % result)

异常捕获的完整语法
try:
    尝试执行的代码
except 错误类型1:
    针对错误类型１对应的代码处理
except 错误类型２:
    针对错误类型2对应的代码处理
except (错误类型３, 错误类型4):
    针对错误类型　３、４对应的代码处理
except Exception as result:
    print(result)
else:
    没有异常时执行的代码
finally:
    无论是否有异常都执行的代码
"""