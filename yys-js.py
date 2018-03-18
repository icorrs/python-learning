#自动打觉醒材料
import pyautogui
import time
import re
from datetime import datetime
def click_onetime():
    x,y=(1377,725)
    time.sleep(5)
    pyautogui.click(x,y,duration=0.2)
    time.sleep(45)
    pyautogui.click(x,y+200,duration=0.2)
def get_click_count():
    click_count=input('enter times:')
    if re.match(r'\d+',click_count):
        return int(click_count)
    else:
        get_click_count()
def click_times():
    click_counts=get_click_count()
    i=1
    time.sleep(5)
    while i<=click_counts:
        click_onetime()
        print('%s : %s'%(i,str(datetime.today()).split(' ')[1]))
        i+=1
    print('finished :%s'%(str(datetime.today()).split(' ')[1]))
if __name__=='__main__':
    click_times()
