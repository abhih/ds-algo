NUMBER=[3002]#,20002]
def check_evenness(i):
    i=str(i)
    for j in range(0,len((i))):
        val=int(i[j:j+1])
        #print(val)
        if val!=" " and val!=None and val%2!=0 :
            #print(val,True)
            return False
    return True

for i in NUMBER:
    if check_evenness(i)==True:
        print(i)
    else:
        print('NOT')