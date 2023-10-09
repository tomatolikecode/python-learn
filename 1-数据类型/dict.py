""""""
'''
字典
可变容器模型,而且可以存储任意类型对象
Key-Value
'''

'''
创建
字典名 = {'key1':'value1','key2':'value',...}
    字典中的每个元素都是‘键(key)值(value)对’,每个键值对使用:分割,每个元素之间用,分割.
    其中键(key)必须是唯一的,如果重复,最后一个的值会替换前边相同键的值
'''
dict0 = dict()
print(type(dict0))  # 类型
dict1 = {'code': 200, 'msg': '重点测试', 'data': ["a", "b", 1]}
print(type(dict1))  # 类型


'''
修改
字典名[键] = 值
    当前键已经存在会修改字典中该键原有的值,不存在时,会创建新的键值对
'''
dict2 = dict()
print(type(dict2))  # 类型
dict2['a'] = 'bb'  # 赋值
dict2[1] = 'cc'  # 赋值
dict2['b'] = 222  # 赋值
print(dict2)

'''
删除
删除某个键值对
    del 字典名[键]
清空字典中所有元素
    字典名.clear()
删除字典
    del 字典名
'''
dict3 = {'code': 200, 'msg': '重点测试', 'data': ["a", "b", 1]}
print("原始数据", dict3)
del dict3["msg"]
print("删除msg", dict3)
dict3.clear()
print("clear 后", dict3)
del dict3
print("dict 被删除了")

'''内置函数及其方法
函数      	            描述
len(dict)	            返回字典元素的个数,即键的个数
str(dict)	            输出字典,以可打印的字符串输出
type(variable)	        返回输入的变量类型
dict.clear()	        清空字典
dict.copy()	            复制字典
dict.fromekey(sep,val)	以sep中元素为键,val中的元素为值,创建一个新字典
dict.get(key)	        返回指定键的值,如果键不存在返回None
dict.items()	        返回字典中的所有键值对
dict.keys()	            返回字典中的所有键
dict.update(dict2)	    将dict2合并到dict
dict.values()	        返回字典中的所有值
'''