import pyautogui
import time
import sys
sound_im=r'c:\python tem\sound.png'
bt_speaker_im=r'c:\python tem\bt_speaker.png'
ft_speaker_im=r'c:\python tem\ft_speaker.png'
default_sp_im=r'c:\python tem\default_sp.png'
default_co_im=r'c:\python tem\default_co.png'
ft_default_im=r'c:\python tem\ft_default.png'
bt_default_im=r'c:\python tem\bt_default.png'
cpicon_num=int(input('please enter control pad ico num:'))-1
speaker_num=str(input('please enter speaker num(1 means fantasia usb speaker,2 means bluetooth speaker):'))
if speaker_num not in ('1','2'):
    print('please enter the right speaker_num(1 means fantasia usb speaker,2 means bluetooth speaker):')
    sys.exit()
else:
    pyautogui.click(80+cpicon_num*62,1060,button='right')
    time.sleep(0.2)
    x,y=pyautogui.center(pyautogui.locateOnScreen(sound_im))
    pyautogui.click(x,y)
    time.sleep(0.8)
    if speaker_num=='1':
        if pyautogui.locateOnScreen(ft_default_im):
            print('ft_speaker is already the default speaker')
            sys.exit()
        else:
            a,b=pyautogui.center(pyautogui.locateOnScreen(ft_speaker_im))
    else:
        if pyautogui.locateOnScreen(bt_default_im):
            print('bt_speaker is already the default speaker')
            sys.exit()
        else:
            a,b=pyautogui.center(pyautogui.locateOnScreen(bt_speaker_im))
    pyautogui.click(a,b,button='right')
    time.sleep(0.2)
    c,d=pyautogui.center(pyautogui.locateOnScreen(default_sp_im))
    pyautogui.click(c,d)
    time.sleep(0.2)
    pyautogui.click(a,b,button='right')
    time.sleep(0.2)
    e,f=pyautogui.center(pyautogui.locateOnScreen(default_co_im))
    pyautogui.click(e,f)
pyautogui.typewrite(['enter'])