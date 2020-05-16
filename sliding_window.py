a='abhishek'
key='is'
for i in range(1,len(a)):
    if a[i-1]+a[i]==key:
        print("found",key)
    else:
        print("not found",a[i-1]+a[i])