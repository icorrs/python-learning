import math
begin=float(input('please enter begin num:'))
ratio=float(input('please enter ratio:'))
num=int(input('please enter num:'))
def geo_seq_sum(begin,ratio,num):
    def_list=[]
    def_sum=0
    for i in range(1,num+1):
        num_i=begin*math.pow(ratio,i-1)
        def_list.append(num_i)
        def_sum+=num_i
    return(def_list,def_sum)
x,y=geo_seq_sum(begin,ratio,num)
print(x)
print(y)
