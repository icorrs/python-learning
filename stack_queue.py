#先确认是stack还是queue，然后实现堆栈/队列，python核心编程6.15节
stack=[]
def push():
    new_string=input('enter new string:')
    stack.append(new_string)
def pop():
    if len(stack)==0:
        print('stack is empty,can\'t pop')
    else:
        stack.pop()
def remove():
    if len(stack)==0:
        pring('stack is empty,can\'t remove')
    else:
        stack.remove(stack[0])
def view():
    print(stack)
dic1={'stack':{'v':view,'u':push,'o':pop},'queue':{'v':view,'u':push,'o':remove}}
pt='''enter choice:
         (q for quit;
         v for view;
         u for push;
         o for pop/remove)'''
pl='''enter mode(stack or queue):'''
how=str(input(pl))
while True:
    choice=input(pt).strip()[0].lower()
    if choice not in 'uovq':
        print('invalid option')
    elif choice=='q':
        break
    else:
        dic1[how][choice]()
