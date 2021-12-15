'''
eval 函数
    将字符串当成一个有效的表达式来求值并返回计算结果
    有效的表达式： 去掉字符串的引号，将字符串内容当成代码看

eg. input_str = input('请输入一个算术题：')

    print(eval(input_str))

eval 慎用 —— 不要使用 eval 直接转换 input 的结果

eg. input_str = input()
    print(eval(input_str))
    输入：
    __import__('os').system('ls')
    __import__('os').system('rm -r *')
    等价于：
        import os
        os.system('ls')
        os.system('rm -r *')   # 会清空当前的所有文件
'''