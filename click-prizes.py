#click fgo nero-prize
import math
import pyautogui
import time

cordination_dic = {'ten_item':(648,636),'reset':(1641,370),
    'confirm':(1215,823),'close':(941,818)}

def time_print(content_str):
    return '%s: %s'%(time.asctime(),content_str)

def click_price(times=130):
    for i in range(times):
        pyautogui.click(cordination_dic['ten_item'][0],cordination_dic['ten_item'][1],duration=0.3)

def click_new_pool():
    time.sleep(5)
    for key in ['reset','confirm','close']:
        pyautogui.click(cordination_dic[key][0],cordination_dic[key][1],duration=3)
    
def click_all_flower():
    flower_num = int(input('please enter flower number:'))
    current_rest = int(input('please enter rest item num in current pool:'))
    if current_rest > 0 and current_rest != 300:
        print(time_print('clicking rest item in current pool...'))
        flower_num = flower_num-current_rest*2
        if flower_num > 0:
            current_click_times = math.ceil(current_rest/10)*4+5
        else:
            current_click_times = math.ceil((current_rest*2+flower_num)/20)*4+5
        time.sleep(5)
        click_price(current_click_times)
        print(time_print('rest item in current pool click finished...'))
        if flower_num > 0:
            click_new_pool()
        else:
            pass
    elif current_rest == 0:
        click_new_pool()
    else:
        pass
    time.sleep(5)
    if flower_num <= 600:
        print(time_print('start click pool...'))
        click_price(math.ceil(flower_num/20)*4+5)
        print(time_print('finished'))
    else:
        i = math.ceil(flower_num/600)
        remain_num = flower_num%600
        for j in range(i-1):
            print(time_print('start print num %s pool...'%(str(j+1))))
            click_price()
            print(time_print('num %s pool click finished'%(str(j+1))))
            click_new_pool()
        click_price(times=math.ceil(remain_num/20)*4+5)
        
if __name__ == '__main__':
    click_all_flower()
