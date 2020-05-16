def split_fn(str_val,split_val):
#str_val=sort(str_val)
    list=[]
    i =0
    x=0
    j=len(str_val)
    if split_val in str_val:
        while(i<j):
            if str_val[i] == split_val:# and str_val[i+1] in split_val  :
                print(str_val[i])
                list.append(str_val[x:i])
                print(str_val[x:i])
                i+=len(split_val)
                x=i
            i+=1
    return list
s1 = 'abcdefcgci'
print("result",split_fn(s1,'c'))
l=s1.split('c')
print(l)