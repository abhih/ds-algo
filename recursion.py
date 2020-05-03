ll=[1,1,1,1,1,1,1,1,1,1]

def agg(remaining):
    if len(remaining)<2:
        return
    initial = remaining[0]
    after = remaining[1]
    if (initial+after)==2:
        print 2
    remaining = remaining[2:]
    return agg(remaining)

#print(agg(ll))

def agg_first_int(n):
    return n*(n+1)//2
def rec_agg_first_int(n):
    if n==0:
        return n
    else:
        print(n-1, n)
        return rec_agg_first_int(n-1)+n
#print(agg_first_int(5))
#print(rec_agg_first_int(5))

##reverse string recursively

def rec_rev_string(n):
    print(n)
    if len(n)==0:
        return n
    
    return n[-1:]+rec_rev_string(n[:-1])
print(rec_rev_string([1,2,3,4,5]))