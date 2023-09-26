""""""
'''
列表
    方括号 [] 之间、用逗号分隔开

创建方式
    列表定义格式: 
        列表名=[元素1, 元素2, ...]
    空列表定义: 
        列表名=[]
    或
        列表名=list()
'''

list0 = list()
list1 = [1, 1.1, "str1", True, [2, False]]
list2 = ["a", "b"]

print(list0)             # 输出完整列表
print(list1[0])          # 输出列表第一个元素
print(list1[1:3])        # 从第二个开始输出到第三个元素
print(list1[2:])         # 输出从第三个元素开始的所有元素
print(list2 * 2)        # 输出两次列表
print(list1 + list2)     # 连接列表

'''
列表删除
1.根据索引删除某个元素
del 列表名[索引]
2.删除列表中某些连续元素
del 列表名[[头下标]:[尾下标]]
    删除的是从头下标开始,到尾下标结束之前的内容。省略头下标默认是从0开始，省略尾下标则是默认到结尾处的所有元素
3.删除列表中所有元素
del 列表名[[头下标]:[尾下标]]

list自带方法
list.index(元素) 获取元素索引
list.insert(序号, 元素) 插入
list.append(元素) 尾部追加 一个
list.extend(list) 尾部追加 一批, 参数为list
'''
li = ['a', [1, "a"], 'b', 'c', 'd', 525]
print(li[0])
# 根据索引删除某个元素
list3 = ['a', 'b', 'c', 'd', 525]
del list3[2]
print(list3)
# 删除列表中某些连续元素
del list3[2:4]
print(list3)
# 删除列表中所有元素
del list3[:]
print(list3)
# 删除  list.pop(下标)
list3.pop(1)
# 删除某个元素
list3.remove('a')

# 列表+, *, in计算
list4 = ['a', 'b', 'c']+[1, 2, 3]    # 结果为['a','b','c',1,2,3]
print(list4)
list5 = [1, 2, 3] * 3                # 结果为[1,2,3,1,2,3,1,2,3]
print(list5)
list6 = 1 in [1, 2, 3]             # 结果为True
print(list6)
# 列表遍历
list7 = [1, 2, 3, 4, 5]
for i in list7:
    print(i, end='')
    # 结果为1 2 3 4 5
"""
相关内置函数
函数	        描述
len(list)	返回列表长度(即列表元素个数)
max(list)	返回列表中最大的元素
min(list)	返回列表中最小的元素
list(sep)	将元组、字典、集合、字符串转换为列表

列表方法
方法	                描述
list.append(obj)	向列表末尾添加对象
list.count(obj)	    统计某个元素在列表中出现的次数
list.extend(sep)	在列表末尾添加另一个序列的值(用新列表扩展原来的列表)
list.index(obj)	    返回列表中查找某个值第一个匹配项的索引值
obj=list.pop()	    移除列表中的一个值(默认为最后一个),并返回移除的值
list.remove(obj)	移除列表中第一个匹配项
list.reverse()	    将列表翻转
list.sort()	        对列表进行排序
list.clear()	    请空列表
list.copy()	        复制列表
"""


