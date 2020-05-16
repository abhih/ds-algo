def reverse_str(val):
    if len(val)==0:
        return val
    print(val)
    return(reverse_str(val[1:])+val[0])
val='abcde'
print(reverse_str(val))