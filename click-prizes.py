#click fgo nero-prize
import math
import pyautogui
import time

cordination_dic = {'ten_item':(648,636),'reset':(1641,370),
    'confirm':(1215,823),'close':(941,818)}

def click_price():
    for i in range(130):
        pyautogui.click(cordination_dic['ten_item'][0],cordination_dic['ten_item'][1],duration=0.3)

def click_new_pool():
    for key in ['reset','confirm','close']:
        pyautogui.click(cordination_dic[key][0],cordination_dic[key][1],duration=3)
    
def click_all_flower():
    flower_num = int(input('please enter flower number:'))
    time.sleep(5)
    if flower_num < 600 or flower_num == 600:
        click_price()
    else:
        i = math.ceil(flower_num/600)
        for j in range(i):
            click_price()
            time.sleep(5)
            click_new_pool()

if __name__ == '__main__':
    click_all_flower()
