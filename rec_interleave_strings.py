#https://www.techiedelight.com/find-interleavings-of-given-strings/
x=0
def rec_interleave_str(var,step=0):
    if len(var)==step:
        global x
        x=x+1
        print(x)
        print(var)
        return var
    for i in range(step,len(var)):
        var=list(var)
        var[i],var[step]=var[step],var[i]
        var="".join(var)
        rec_interleave_str(var,step+1)

val="ABC"
print(rec_interleave_str(val))