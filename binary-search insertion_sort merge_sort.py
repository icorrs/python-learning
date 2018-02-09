#write code of insertion_sort when learning chapter2 of <introduction to algorithms> 
import math
def binary_search(source_num,source_list):
    first_part=source_list[:math.ceil(len(source_list)/2)]
    second_part=source_list[math.ceil(len(source_list)/2):]
    if source_num>=first_part[-1] and source_num<=second_part[0]:
        return (first_part[-1],second_part[0])
    else:
        if source_num<first_part[-1]:
            source_list=first_part
            return binary_search(source_num,first_part)
        else:
            source_lst=second_part
            return binary_search(source_num,second_part)
print(binary_search(5,[1,3,5,7,9,10]))
def insertion_sort(source_list):
    def_list=[source_list[0]]
    for i in range(1,len(source_list)):
        if source_list[i]<=def_list[0]:
            def_list.insert(0,source_list[i])
        elif source_list[i]>=def_list[len(def_list)-1]:
            def_list.append(source_list[i])
        else:
            x,y=binary_search(source_list[i],def_list)
            def_list.insert(def_list.index(y),source_list[i])
    return def_list
print(insertion_sort([1,0.5,5,3,6,7,0.4,2]))
def merge(list1,list2):
    def_list=[]
    while len(list1)>0 and len(list2)>0:
        if list1[0]<=list2[0]:
            def_list.append(list1[0])
            list1.remove(list1[0])
        else:
            def_list.append(list2[0])
            list2.remove(list2[0])
    def_list.extend(list1)
    def_list.extend(list2)
    return def_list
print(merge([1,2,5,6],[2,3,4,7]))
def merge_sort(list1):
    if len(list1)>1:
        slice_indice=int(len(list1)/2)
        list1_left=list1[:slice_indice]
        list1_right=list1[slice_indice:]
        return merge(merge_sort(list1_left),merge_sort(list1_right))
    else:
        return list1
print(merge_sort([1,3,2,5,8,7]))



