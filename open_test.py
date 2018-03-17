#test diffrent functions of access_mode of attribute open. 
dic_openmode={1:'r',2:'w',3:'a',4:'r+',5:'w+',6:'a+'}
mode=int(input("""enter mode num:
01 for 'r'
02 for 'w'
03 for 'a'
04 for 'r+'
05 for 'w+'
06 for 'a+':"""))
f=open(r'c:\python tem\open_test.txt',dic_openmode[mode],encoding='utf-8')
try:
    f.write('add')
except IOError:
    print('error')
f.close()
