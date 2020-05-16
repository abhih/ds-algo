ll=["abc","abdc","abhishek","bac","badc","hashbike"]
length=len(ll)
def hashfunction(val):
    sum_ele=sum([ord(i)+j for j,i in enumerate(val)])
    sum_ele=sum_ele%length
    return sum_ele
index=(list((map(hashfunction,ll))))
print(index)
maptable={}
for ix,val in zip(index,ll):
    print(ix,"\t",val)
    if ix not in maptable:
        maptable[ix]=val
    else:
        maptable[ix]=[maptable.get(ix),str(val)]
print(maptable) 