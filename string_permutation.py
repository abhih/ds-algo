temp=0
def str_permute(val):
    if (val)==0:
        return "DOne"
    print(val)
    print(str_permute(val-1))
    return val

print(str_permute(2))
