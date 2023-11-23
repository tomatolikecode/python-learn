# 单行文本
import calendar

letter = "single letter"
print(letter)
print(len(letter))
letter2 = ("a"
           "b"
           "c")
print(letter2)
print(len(letter2))
# 多行文本

multiline2 = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.
"""
print(multiline2)

# 字符串凭借, +
first_name = "tomato"
last_name = "potato"
full_name = first_name + " " + last_name
print(full_name)

# 解包字符
language = "python"
a, b, c, d, e, f = language
print(a, b, c, d, e, f)

print(language[2])      # 正向, 从0开始
print(language[-2])     # 反向, 从-1开始

# 变量[头下标:尾下标(不取)]
# python
# 012345
print(language[:])      # python    全部
print(language[2:])     # thon      从2号位开始
print(language[:5])     # pytho
print(language[1:3])    # yt
# p  y  t  h  o  n
# -6 -5 -4 -3 -2 -1
print(language[-1:])    # n
print(language[-4:-1])    # tho
print(language[-6:])    # python

# 拆分Python字符串时跳过字符
# python
# 012345
print(language[0:6:2])     # pto
print(language[0:6:3])     # ph

# 转义字符 \n \r \t \\ \"
print('I hope every one enjoying the python challenge.\nDo you ?')
print('Days\tTopics\tExercises')
print('Day\t\t1\t\t3\t\t5')
print('This is a back slash  symbol (\\)')
print('In every programming language it starts with \"Hello, World!\"')

"""
字符串方法
"""
print("字符串方法")
challenge = 'thirty days of python'

# capitalize() 将字符串中的第一个字符转换为大写字母
print("capitalize(): ", challenge.capitalize())   # Thirty days of python

# count(x:str, __start:int, __end:int): 返回字符串中子字符串的出现次数
print("count(): ", challenge.count('y'))
print("count(): ", challenge.count('y', 2, len(challenge)))
print("count(): ", challenge.count('th'))

# endswith(str): 检查字符串是否以指定的结尾结束
print("endswith(): ", challenge.endswith('on'))         # True
print("endswith(): ", challenge.endswith('pytho'))      # False

# startswith(str): 检查字符串是否以指定的开头
print(challenge.startswith('thirty'))   # True
other_challenge = '30 days of python'
print(other_challenge.startswith('thirty'))   # False

# expandtabs(tabsize:int): 用空格替换制表符，默认制表符大小为8。它采用制表符大小参数
tempData = 'thirty\tdays\tof\tpython'
print("expandtabs(): ", tempData.expandtabs())  # thirty  days    of      python
print("expandtabs(): ", tempData.expandtabs(3))  # thirty  days    of      python

# find(str): 返回子字符串第一次出现的索引, -1 表示没找到
print("find(): ", challenge.find('r'))      # 3
print("find(): ", challenge.find("th"))     # 0
print("find(): ", challenge.find("zon"))    # -1

# format(): 将字符串格式化为更好的输出, 依次填入, 多余的忽略
first_name = 'tomato'
last_name = 'potato'
job = 'teacher'
age = 25
sentence = 'my name is {} {}. i am a {}, age is {}'
new_sentence = sentence.format(first_name, last_name, job, age, "bbbaa")
print("format(): ", new_sentence)
new_sentence = sentence.format(first_name, last_name, job, str(age))  # 建议数据转成str
print("format(): ", new_sentence)


# print(": ",)