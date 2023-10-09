class Employee:
    code = 66 # 静态变量, Employee.code, 实例对象.code 可改变
    # 成员变量
    salary = 0
    name = ""

    def __init__(self, name: str, salary: float):
        """
        构造方法,  指定变量属性
        :param name:
        :param salary:
        """
        self.name = name
        self.salary = salary

    def say(self):
        """
        问好方法
        :return: str
        """
        print("hello, i am %s" % self.name)

    def string(self):
        """
        问好方法
        :return: str
        """
        print("name: %s, salary %f" % (self.name, self.salary))


# 初始化对象
emp = Employee
print(emp)
emp0 = Employee("Amy", 6666)
print(emp0)
print(emp0.name)
print(emp0.salary)
emp1 = Employee(name="John", salary=7777)
# 调用方法
emp1.say()

# 更新变量值
emp1.name = "山岚"
emp1.say()

# 给对象添加一个新成员变量, 这个新成员变量只对emp1实例化有效
emp1.addone = 1
print(emp1.addone)

# 检查和校验对象类型
e1 = Employee("a", 1)
e2 = Employee("b", 2)
print("e1:", type(e1))
print("e2:", type(e2))
print("compare:", type(e1) is type(e2))

# 对象所有属性赋值到另一个对象
em1 = Employee("a", 1)
em2 = Employee("b", 2)
em1.string()
em1.msg = "hallelujah"
print("em1.msg: ", em1.msg)
em1.string()
em2.string()

em2.__dict__.update(em1.__dict__)
em2.string()
print("em2.msg: ", em2.msg)

# 打印对象所有属性
emp3 = Employee("Lina", 89874)
temp = vars(emp3)
for item in temp:
    print(item, ":", temp[item])


# 运行时创建类的属性
class Student:
    pass


stu = Student()
setattr(stu, 'Age', 25)
setattr(stu, 'Phone', "110")
print(stu.Age)
print(stu.Phone)


# 在函数中将对象的实列作为参数传递
class Vehicle:
    def __init__(self):
        self.trucks = []

    def add_trucks(self, truck):
        self.trucks.append(truck)


class Truck:
    def __init__(self, color: str):
        self.color = color

    def __repr__(self):
        return "{}".format(self.color)


def main():
    v = Vehicle()
    msg = "Red Blue Green"
    for i in msg.split():
        t = Truck(i)
        v.add_trucks(t)

    print(v.trucks)




