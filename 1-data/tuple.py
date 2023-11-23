""""""
'''
元组
内容不可篡改
语法: (元素, 元素, ...)
'''
tuple0 = tuple()
print(type(tuple0))
tuple1 = (1, "a", 3)
print(tuple1)
print(type(tuple1))

# 元组操作
# 1.index查找方法
index = tuple1.index(3)
print("index: ", index)

# 2.count统计方法
c = tuple1.count(3)
print("count", c)

# 3.len函数统计元组元素数量
num = len(tuple1)
print("len: ", num)

# 遍历1
for data in tuple1:
    print(data, end=" ")


# 遍历2
i = 0
while i < len(tuple1):
    print("msg:", tuple1[i])
    i += 1

