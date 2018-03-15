#I have a whole cdimage's cue file that without track's title message in it(althoug index message is complete) .\
# This script read track list of this cd and add title to cue file.
import re
f1=open(r'D:\music\久石让\魔女宅急送\list.TXT', 'r')
f2=open(r'D:\music\久石让\魔女宅急送\CDImage.cue', 'r')
list_title=list(f1)
f1.close()
list_cue=list(f2)
f2.close()
cue_out=open(r'c:\python tem\cue_out.txt','w',encoding='utf-8')
pat_title=re.compile(r'(\d{2})\.(.+)?(\[.+\]\n$)')
dic_title={}
for line in list_title:
    if re.match(pat_title,line):
        dic_title[int(re.match(pat_title,line).group(1))]=re.match(pat_title,line).group(2).strip()
    else:
        pass
pat_track=re.compile(r'\s+TRACK\s+(\d+)')
dic_track={}
for line in list_cue:
    if re.match(pat_track,line):
        dic_track[int(re.match(pat_track,line).group(1))]=list_cue.index(line)
    else:
        pass
for i in range(3):
    cue_out.write(list_cue[i])
for i in range(len(dic_track)-1):
    cue_out.write(list_cue[dic_track[i+1]])
    cue_out.write('    TITLE \"%s\"\n'%(dic_title[i+1]))
    for j in range(dic_track[i+1],dic_track[i+2]-1):
        if not list_cue[j+1].strip().startswith('TITLE'):
            cue_out.write(list_cue[j+1])
        else:
            pass
cue_out.write(list_cue[-2])
cue_out.write('    TITLE \"%s\"\n'%(dic_title[len(dic_title)]))
cue_out.write(list_cue[-1])
cue_out.close()
