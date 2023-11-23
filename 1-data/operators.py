# 操作符

# 整形数据
print("整形数据")
print("Addition: ", 1 + 2)  # 加法
print("Subtraction: ", 1 - 2)  # 减法
print("Multiplication: ", 3 * 2)  # 乘法
print("Division: ", 4 / 2)  # 除法, 有小数点, 返回float类型
print("Division: ", 0.1 / 2)  #
print("Division without the remainder: ", 1 // 2)  # 除法, 取整
print("Division without the remainder: ", 11 // 3)  #
print("Modulus: ", 1 % 2)  # 取余
print("Exponential: ", 3 ** 2)  # 幂等 3的2次方

# 浮点数据
print("浮点数据")
print("Floating: ", 3.14)

# 复数
print("复数")
print("Complex: ", (1 + 3j) * (1 - 2j))

# 首先在顶部声明变量
a = 1
b = 2

# 算术运算并将结果分配给变量
print("算术运算并将结果分配给变量")
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# 比较
print("比较")
print(2 < 3)
print(2 <= 3)
print(2 > 3)
print(2 >= 3)
print(2 == 3)
print(2 != 3)

# 布尔类型的比较
print("布尔类型的比较")
print("T == T: ", True == True)
print("T == F: ", True == False)
print("F == F: ", False == False)
print("T and T: ", True and True)
print("T or F: ", True or False)

# 其他方式的运算
print("其他方式的运算")
print("1 is 1: ", 1 is 1)
print("1 is not 2: ", 1 is not 2)
print("A in Abc: ", 'A' in 'Abc')
print("B in Abc: ", "B" in "Abc")
print("hello in helloworld: ", "hello" in "helloworld")
print("4 is 2 ** 2: ", 4 is 2 ** 2)
# print("2 in 4: ", 2 in 4)  数值不能用in

print(2 < 5 < 4)        # True
print(3 > 2 and 4 < 3)  # False
print(2 > 3 > 4)        # False
print(3 > 2 or 4 > 3)   # True
print(3 > 2 or 4 < 3)   # True
print(3 < 2 or 4 < 3)   # False
print(not 3 > 2)        # False
print(not True)         # False
print(not False)        # True
print(not not True)     # True
print(not not False)    # False

'''
算术运算符优先级  从上到下依次降低
**	                                        幂运算
*、/、%、//	                                乘、除、取余、取整
+、-	                                    加、减
<、>、<=、>=、==、!=、is、is not、in、not in	比较运算符、身份运算符、成员运算符
not	                                        逻辑运算符 not
and	                                        逻辑运算符 and
or	                                        逻辑运算符 or
=、+=、-=、*=、/=、%=、//=、**=	            赋值运算符
'''
