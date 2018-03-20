#test closure
#closure part
def foo(y=0):
    x=[y]
    #if use x=y,will return unboundLocalError when use bar(),because in x=y,x is int object,can't be changed in bar().list it or use nonlocal will be ok.\
    #如果用x=y的方式引用，那么在内嵌函数bar中对x修改x+=1会发生诸如函数修改全局变量的问题“unboundlocalerror”，\
    #解决办法是1：像书中例子一样，list化，变为可变对象。2：像本地函数通过global声明对全局变量进行修改，内嵌函数通过nonlocal声明对嵌套作用域中变量进行修改
    print('foo id:%s;x id:%s'%(id(foo),id(x)))
    def bar():
        x[0]+=1
        print('bar id:%s;x id:%s'%(id(bar),id(x)))
        return x[0]
    return bar
#print('outer x id:%s'%(id(x)))
count=foo(5)
print(id(count),count.__closure__)
count1=foo(6)
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
#non closure part
def foo1(y):
    return list(y)
print('id foo1:%s'%(id(foo1)))
count1=foo1
print('id count1:%s'%(id(count1)))
print(count1('abc'))
count2=foo1
print('id count2:%s'%(id(count2)))
print(count1('def'))
