'''
字典 dict {} 除列表外最灵活的数据类型
            通常用于存储描述一个物体的相关信息
列表 —— 有序的对象集合
字典 —— 无序的对象集合

字典使用键值对存储数据，键值对之间用 , 分隔
    1) 键 key 是索引
    2）值 value 是数据
    3）键值之间使用 : 分隔
    4）键必须是唯一的
    5）值可以取任何数据类型，但键只能使用 字符串、数字或元组
'''

person_dict = {'name': 'pel', 'age': 28, "height": 175}
person_dict1 = {'name': 'pel', 'age': 30, "height": 175}
print(person_dict['name'])
person_dict['weight'] = 140  #
person_dict.setdefault('weight', 136)
#person_dict.update(person_dict1)
person_dict1.update(person_dict)
print(person_dict)
print(person_dict1)

'''
字典名[key]    value
字典名[key] = value    key 不存在时，新增/ key 存在时，修改字典
字典名.setdefault(key, value)  key 存在，不修改数据；key 不存在，新增
del 字典名[key]  删除字典中的某个键值对
字典名.popitem()  随机删除一个键值对
字典名.pop(key)  删除键值对
len(字典名)  统计键值对的数量
字典名.update(字典1)  合并字典，如果被合并的字典中包含已存在的键值对，会覆盖原有的
字典名.clear()  清空
字典名.get(key)  取值，key 不存在，不报错
字典名.items()  所有 (key, value) 元组列表
字典名.values()  所有 value 列表

'''
