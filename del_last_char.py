def del_last_char(source_word):
    i=len(list(source_word))
    def_list=[]
    while i>0:
        def_list.append(source_word[:i])
        i-=1
    return def_list
print(del_last_char('abcdefg'))
