import pyautogui
import time
ico_num=int(input('please enter ico_num:'))-1
del_num=int(input('please enter del_num:'))
pyautogui.click(80+ico_num*62,1060,button='right')
for i in range(1,del_num+1):
    pyautogui.click(80+ico_num*62,933,button='right')
    time.sleep(0.2)
    x,y=pyautogui.center(pyautogui.locateOnScreen(r'c:\python tem\del_from_list.png'))
    pyautogui.click(x,y)
    i+=1
    time.sleep(0.2)
print('finished,have delete %s readed list.'%(del_num))