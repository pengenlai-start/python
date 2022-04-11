"""
不要在切片里同时指定起止下标与步进

1. 同时指定切片的起止下标与步进值理解起来会很困难
2. 如果要指定步进值，那就省略起止下标，而且最好采用整数作为步进值，尽量别用负数（步进值为负数时，从末尾向前取数）
3. 不要把起始位置、终止位置与步进值全都写在同一个切片操作里。如果必须同时用这三项指标，那就分两次来做（其中一次隔位选取，另一次做切割），
也可以改用 itertools 内置模块里的 islice 方法
"""
