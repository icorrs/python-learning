#click fgo nero-prize
import math
import pyautogui
import time

cordination_dic = {'ten_item':(648,636),'reset':(1641,370),
    'confirm':(1215,823),'close':(941,818)}

def time_print(content_str):
    print('%s: %s'%(time.asctime(),content_str))

def get_num(num_str,**kw):
    out_num = float(input('please enter %s:'%(num_str)))
    if 'max_num' in kw.keys():
        max_entered = kw['max_num']
        if out_num <= max_entered:
            pass
        else:
            print('wrong number entered,the number must no more than %s'%(max_entered))
            get_num(num_str,**kw)
    if 'min_num' in kw.keys():
        min_entered = kw['min_num']
        if out_num >= min_entered:
            return out_num
        else:
            print('wrong number entered,the number must no less than %s'%(min_entered))
            get_num(num_str,**kw)

def click_prize(times=130):
    for i in range(times):
        pyautogui.click(cordination_dic['ten_item'][0],cordination_dic['ten_item'][1],duration=0.3)

def click_new_pool():
    time.sleep(5)
    for key in ['reset','confirm','close']:
        pyautogui.click(cordination_dic[key][0],cordination_dic[key][1],duration=3)

flower_num_input = get_num('the flower\'s total num',**{'min_num':0,'max_num':6000})
rest_item_input = get_num('the item num that left in current pool',**{'min_num':0,'max_num':300})
pool_nums = 0

def click_prize_recursive(flower_num,rest_item=300):
    if rest_item == 0:
        click_new_pool()
        rest_item = 300
        click_prize_recursive(flower_num)
    elif flower_num <= rest_item*2:
        time_print('click the last pool:')
        time.sleep(5)
        click_prize(math.ceil(flower_num*0.2)+5)
        time_print('finished')
    else:
        global pool_nums 
        pool_nums += 1
        time_print('begin to click num %s pool...'%(pool_nums))
        time.sleep(5)
        click_prize(math.ceil(rest_item*0.4)+5)
        time_print('num %s pool finished...'%(pool_nums))
        flower_num = flower_num-rest_item*2
        click_new_pool()
        click_prize_recursive(flower_num)
        
if __name__ == '__main__':
    click_prize_recursive(flower_num_input,rest_item_input)
