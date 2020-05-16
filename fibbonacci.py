n=4
def fibb(n):
    if n==0 or n==1:
        return n
    a=0
    b=1
    print(a)
    for i in range(1,n):
        print(b)
        a,b=b,a+b
    return b

def fibb_rec(n):
    if n==0 or n==1:
        return n
    return fibb_rec(n-1)+fibb_rec(n-2)
print(fibb(n))
print(fibb_rec(n))