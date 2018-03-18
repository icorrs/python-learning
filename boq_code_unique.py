#公路工程工程量清单编码默认格式母节点为数字型式，子节点为-b字母形式，为使编码唯一便于数据处理，编制此脚本
import re
import pandas as pd
import os
def get_csv_path():#原编码保存为csv文件的一列，便于读取
    path=input('enter csv path:')
    if os.path.isfile(path):
        return path
    else:
        print('csv file not exsit,try again:')
        return get_csv_path()
def unique_code():
    path=get_csv_path()
    path_dir=os.path.dirname(path)
    frame1=pd.read_csv(path,encoding='utf-8')
    list1=list(frame1.iloc[:,0])
    pat1=re.compile(r'\d+-\d+')#数字打头的母节点匹配符
    pat2=re.compile(r'-\D{1}-\d+')#二级子节点，即-字母-数字形式匹配符
    list2=[]
    i=100
    for code in list1:
        if code=='':
            list2.append(i)
            i+=100
        elif re.match(pat1,code):
            cover=code
            list2.append(cover)
        else:
            list2.append(cover+code)
    frame2=pd.DataFrame(list2,)
    frame2.to_csv(os.path.join(path_dir,'code_csv_out.csv'),encoding='utf-8-sig')
if __name__=='__main__':
    unique_code()
