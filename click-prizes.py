#click fgo chrismas-prize
sockes_num=int(input('please enter socket num:'))
import pyautogui
import time
time.sleep(5)
x1,y1=(1661,292)
x2,y2=(1217,817)
x3,y3=(946,812)
x4,y4=(637,651)
def click_prizes():
    for i in range(1,500):
        pyautogui.click(x4,y4,duration=0.3)
def click_newprizes():
    pyautogui.click(x1,y1,duration=2)
    pyautogui.click(x2,y2,duration=2)
    pyautogui.click(x3,y3,duration=2)
if sockes_num<800:
    click_prizes()
else:
    for i in range(1,int(sockes_num/800)):
        click_newprizes()
        click_prizes()
