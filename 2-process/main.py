"""
基本数据类型
    Number      数字
    String      字符串
    bool        布尔类型
    List        列表
    Tuple       元组
    Set         集合
    Dictionary  字典

不可变数据: Number, String, Tuple
可变数据: List, Dictionary, Set
"""

# number 支持 int、float、bool、complex（复数）
a, b, c, d = 20, 2.2, True, 4+3j
print(type(a), type(b), type(c), type(d))
print(isinstance(a, int))

'''
isinstance 和 type 的区别在于：
    type()不会认为子类是一种父类类型。
    isinstance()会认为子类是一种父类类型。
    
bool 是 int 的子类, True 和 False 可以和数字相加,  
True==1, False==0 会返回 True, 但可以通过 is 来判断类型
'''



