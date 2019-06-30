# _*_ coding=utf-8 _*_


from test import *

"""
单个下划线_开头的变量不会被import*导入
单个下划线_开头的变量表示为临时变量，无关紧要的变量
"""
_b = 'Bubble'
c = 'Bool'
# print(a)
# print(_a) 报错name '_a' is not defined


"""
类里面：
1._foo:单个下划线_开头的属性为受保护的成员，不应该被调用。实际上子类和实例都可以访问
2.__foo:双下划线__开头的属性只能在类内部访问，其子类和实例也无法直接访问。
        可以通过方法间接访问,self.__属性
3.__foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的
"""


class Foo():
    _name = "alex"
    __name = "ric"

    def get_name(self):
        print(self.__name)


class Bar(Foo):
    pass


f = Foo()
b = Bar()
b.get_name()
print(b._name)
print(f._name)
# print(b.__name)
