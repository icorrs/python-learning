# templates.py
import re
sco={}
def replacement(m):
    code=m.group(1)
    try:
        return str(eval(code,sco))
    except:
        exec code in sco
        return ''
list1=['[x=1]','[y=2]','the sum of [x] and [y] is [x+y]']
str1=''
for i in list1:
    str1+=i
str2=re.sub(r'\[(.+?)\]',replacement,str1)
print(str2)