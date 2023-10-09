""""""

# 控制台输入
msg = input("请输入:")
print("输入的数据:", msg)

# 普通打印数据
print(1)
print("a")
bool0 = True
print(bool0)
list0 = ["a", "b"]
print(list0)
tuple0 = {"msg": "啊啊谔谔", "code": 200}
print(tuple0)

# 格式化输出, 利用%, %标记转换说明符的开始
msg = "数据"
print("msg: %s" % msg)

code = 200
print("code: %d, msg: %s" % (code, msg))
'''
(1) %字符：标记转换说明符的开始
(2) 转换标志：-表示左对齐；+表示在转换值之前要加上正负号；“”（空白字符）表示正数之前保留空格；0表示转换值若位数不够则用0填充
(3) 最小字段宽度：转换后的字符串至少应该具有该值指定的宽度。如果是*，则宽度会从值元组中读出。
(4) 点(.)后跟精度值：如果转换的是实数，精度值就表示出现在小数点后的位数。如果转换的是字符串，那么该数字就表示最大字段宽度。如果是*，那么精度将从元组中读出
(5) 字符串格式化转换类型

转换类型         含义
d,i         带符号的十进制整数
o           不带符号的八进制
u           不带符号的十进制
x           不带符号的十六进制（小写）
X           不带符号的十六进制（大写）
e           科学计数法表示的浮点数（小写）
E           科学计数法表示的浮点数（大写）
f,F         十进制浮点数
g           如果指数大于-4或者小于精度值则和e相同，其他情况和f相同
G           如果指数大于-4或者小于精度值则和E相同，其他情况和F相同
C           单字符（接受整数或者单字符字符串）
r           字符串（使用repr转换任意python对象)
s           字符串（使用str转换任意python对象）
'''
pi = 3.14159653
print("%10.3f" % pi)            # 字段宽为10, 精度3
print("pi = %.*f" % (3, pi))    # 用*从后面的元组中读取字段宽度或精度
print("%010.3f" % pi)           # 字段宽为10, 用0填充空白, 精度3
print('%-10.3f' % pi)           # 左对齐
print('%+f' % pi)               # 显示正负号


# 结尾不换行, 末尾加上  end = ''
print('我没有换行', end='')

