#计算指定文件夹中扩展名为.py的文件的总行数并生成csv文件.Count line numbers of .py file in specified path and save in csv file.
import os
import pandas as pd
from datetime import datetime
import re
def get_path():#get path need to be processed
    path=str(input('please enter path(a for temppy):'))
    if path=='a':
        path=r'c:\users\mzj\desktop\temppy'
        return path
    if not os.path.isfile(path) and not os.path.isdir(path):
        print('the path entered not exsit')
        get_path()
    else:
        return path
def get_listmode():#get list mode to control if it is need to list the name of file not .py in csv
    list_mode=int(input("""
    please enter list_mode:
    1 for keep the file path not py in csv;
    2 for not keep:"""))
    if list_mode not in (1,2):
        print('enter error')
        get_listmode()
    else:
        return list_mode
def count_lines(file):#count line number of file endswith .py;if not, return 0.
    if file.endswith('.py') or file.endswith('.js'):
        f=open(file,'r',encoding='utf-8')
        lines=len(f.readlines())
        f.close()
        return lines
    else:
        return 0
def list_dir(dir):#count line number of a dir.return list of tuple that tuple[0] is path and tuple[1] is line number
    list_path=os.listdir(dir)
    list_count=[]
    list_file=[os.path.join(dir,x) for x in list_path]
    for file in list_file:
        if os.path.isfile(file):
            list_count.append((file,count_lines(file)))
        else:
            list_count.extend(list_dir(file))
    return list_count
def py_count():#main function 
    path=get_path()
    list_mode=get_listmode()
    list_count=[]
    if os.path.isfile(path):#if the path entered is a file count line number of it
        if os.path.splitext(os.path.split(path))[1] in ('.py','.js'):
            list_count.append((path,count_lines(path)))
            print('%s :%i'%(list_count[0][0],list_count[0][1]))
            print('total:%i'%(list_count[0][1]))
        else:
            print('Error:%s is a file but not a .py file'%(path))
        path=os.path.dirname(path)#if path isfile,change path to it's dirname,so can be used in to_csv.
    else:
        list_count=list_dir(path)
        for path1,value in list_count:
            print('%s :%i'%(path1,value))
        print('total:%i'%(sum([x[1] for x in list_count])))
    frame1=pd.DataFrame(list_count,columns=['path','line_num'])
    frame1.loc[:,'filename']=frame1.loc[:,'path'].map(lambda x:re.match(r'(.+)\\(.+)',str(x)).group(2))
    frame1.loc[:,'filepath']=frame1.loc[:,'path'].map(lambda x:re.match(r'(.+)\\(.+)',str(x)).group(1))
    if list_mode==2:
        frame1=frame1[frame1.loc[:,'line_num']>0]
    else:
        pass
    frame1.to_csv(os.path.join(path,'py_count %s.csv'%(str(datetime.now()).replace(':',' '))),encoding='utf-8')
if __name__=='__main__':
    py_count()
