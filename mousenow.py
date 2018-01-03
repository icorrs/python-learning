import pyautogui
import time
i=1
coordinate_dic={}
try:
    while i:
        time.sleep(5)
        x,y=pyautogui.position()
        positionStr='position'+str(i)+' x:'+str(x)+'; y:'+str(y)+'\n'
        print(positionStr,end='')
        coordinate_dic.setdefault('position'+str(i),(x,y))
        i+=1
        #print('\b'*len(positionStr),end='',flush=True) #原书本行代码用于清空前面取值，只显示最后取值；在自带ide中显示错误
except KeyboardInterrupt():
    print('\ndone')
#print(positionStr,end='')#原书本行代码打印最后一次取值
print(coordinate_dic)
