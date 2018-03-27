#自动打觉醒材料\御魂。默认环境：模拟器或桌面版，电脑分辨率1920*1080


import pyautogui
import time
import re
from datetime import datetime


def click_onetime(dur_time):
    '定义单次操作，其中dur_time为单次通关所需时间'
    x,y=(1377,725)
    time.sleep(5)
    pyautogui.click(x,y,duration=0.2)
    time.sleep(dur_time+20)
    pyautogui.click(x,y+200,duration=0.2)


def get_click_count():
    '获取拟通关次数'
    click_count=input('enter times:')
    if re.match(r'\d+',click_count):
        return int(click_count)
    else:
        get_click_count()


def get_mode():
    '获取打御魂还是打觉醒,1则御魂，2则觉醒'
    mode_num=input('enter mode_num(1 for 御魂;2 for 觉醒):')
    if mode_num=='1' or mode_num=='2':
        return mode_num
    else:
        get_mode()


def click_times():
    '主程序'
    click_counts=get_click_count()
    mode_num=get_mode()
    if mode_num=='1':
        click_one=int(input('输入单次御魂所需时间'))
    else:
        click_one=int(input('输入单次觉醒所需时间'))
    i=1
    time.sleep(5)
    while i<=click_counts:
        click_onetime(click_one)
        print('%s : %s'%(i,str(datetime.today()).split(' ')[1]))
        i+=1
    print('finished :%s'%(str(datetime.today()).split(' ')[1]))


if __name__=='__main__':
    click_times()
