'''
list 列表 <==> 数组，用 [] 定义，数据之间用 , 分隔，可以存储不同类型的数据
'''

num_list = [1, 2, 3, 9]
length = len(num_list)
print("length = %d" % length)

count = num_list.count(3)
print("count = %d" % count)

num_list.append(5)
print(num_list)

num_list.sort()
print(num_list)

num_list.sort(reverse=True)
print(num_list)

num_list.reverse()
print(num_list)

print(num_list[0])

'''
列表.index(数据) 获得数据第一次出现的索引
del 列表[索引] 删除指定索引的数据
列表.remove(数据) 删除第一个出现的指定数据
列表.pop(索引) 删除指定索引的数据
列表.pop() 删除末尾的数据
列表.insert(索引，数据) 指定位置插入数据
列表.append(数据) 在末尾追加数据
列表.extend(列表2) 将列表2的数据追加到列表中

del 关键字本质上是将一个变量从内存中删除
关键字后面不需要使用括号 
'''

