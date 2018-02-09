import pyautogui
import time
times=int(input('please enter click times:'))
time.sleep(5)
for i in range(1,times+1):
    pyautogui.click(1188,845,duration=0.8)
    pyautogui.click(1188,845,duration=0.5)
    time.sleep(3.5)
    pyautogui.click(1106,976,duration=1)
    pyautogui.click(1106,976,duration=1)