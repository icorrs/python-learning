#click fgo chrismas-prize
import pyautogui
import time
time.sleep(5)
x,y=pyautogui.position()
time.sleep(2)
i=1
try:
    while i:
        pyautogui.click(x,y,duration=0.3)
        i+=1
except KeyboardInterrupt():
    print('quit by keyboard')