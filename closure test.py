#test closure
#closure part1；计数器，嵌套函数引用母函数列表变量
x=99
def foo(y=0):
    x=[y]
    print('foo id:%s;x id:%s'%(id(foo),id(x)))
    def bar():
        x[0]+=1
        print('bar id:%s;x id:%s'%(id(bar),id(x)))
        return x[0]
    return bar
count=foo(5)
print(id(count),count.__closure__)
count1=foo(5)#即使count1=foo(5)，count和count1的id也不一样
print(id(count1),count1.__closure__)
del foo
print(count())
print(count())
print(count1())
print(count1())
try:
    print(foo(5))
except NameError:
    print('tried foo(5) but nameerror:foo doesn\'t exist')
#closure part2；无法计数器，嵌套函数引用母函数标量变量
def foo2(y=0):
    x=y
    print('foo2 id:%s;x id:%s'%(id(foo2),id(x)))
    def bar():
        z=x
        z+=1
        print('bar id:%s;x id:%s'%(id(bar),id(x)))
        return z
    return bar
count=foo2(5)
print(id(count),count.__closure__)
count1=foo2(5)
print(id(count1),count1.__closure__)
del foo2
print(count())
print(count())
print(count1())
print(count1())
#closure part3；计数器，嵌套函数引用母函数标量变量，但用nonlocal使得嵌套函数能修改母函数标量变量
def foo3(y=0):
    x=y
    print('foo3 id:%s;x id:%s'%(id(foo3),id(x)))
    def bar():
        nonlocal x
        x+=1
        print('bar id:%s;x id:%s'%(id(bar),id(x)))
        return x
    return bar
count=foo3(5)
print(id(count),count.__closure__)
count1=foo3(5)
print(id(count1),count1.__closure__)
del foo3
print(count())
print(count())
print(count1())
print(count1())
#non closure part
def foo1():
    try:
        x+=1
        return x
    except UnboundLocalError:
        print('error')
print('id foo1:%s'%(id(foo1)))
count1=foo1
print('id count1:%s'%(id(count1)))
print(count1())
count2=foo1
print('id count2:%s'%(id(count2)))
print(count1())
#结论：本test结合核心编程第二版p298、p301、p304、p277
# 1、普通函数（非嵌套）
# 1.1除非用global声明，否则无法对外部标量变量进行直接修改。如果在函数中赋值声明，则生成独立作用域，无法作用于全局；不声明直接修改会引起UnboundLocalError;例如foo1的情况\
# 1.2外部变量为可变类型对象时，函数可以直接修改外部变量。
# 2、嵌套函数
# 2.1 嵌套函数未必都是闭包，例如单纯增加时间戳的装饰器就不是闭包；只有嵌套函数引用了母函数变量时，嵌套函数才成为闭包；
# 2.2 当为闭包时，对母函数的引用会直接运行母函数部分并将闭包数据初始化（即如foo例子中，只是count=foo，就会触发母函数运行）。此时即使del母函数，闭包所引用的变量依然保存在其作用域中。\
#     对母函数的调用时才会运行闭包部分；
# 2.3 闭包状态下，嵌套函数可直接修改母函数的可变对象变量，但初始化只有一次，以后都是累加，例如closure part1，foo函数
# 2.4 闭包状态下，嵌套函数不可直接修改母函数的标量变量，例如closure part2，foo2函数；
# 2.5 闭包状态下，声明nonlocal的情况下，嵌套函数可修改母函数的标量变量，例如closure part3，foo3函数。但如global一样，不推荐使用。