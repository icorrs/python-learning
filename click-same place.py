import pyautogui
import time
click_num=int(input('please enter click times:'))
time.sleep(5)
x,y=pyautogui.position()
for i in range(1,click_num+1):
    pyautogui.click(x,y,duration=0.3)
