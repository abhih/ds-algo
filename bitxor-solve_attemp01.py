M=5
N=8
arr=[i for i in range(M,N+1)]
print(arr)
if len(arr)%2==0:
    print("y")
    arr1=[(arr[i],arr[i+1]) for i in range(0,len(arr),2)]
    arr2=[(arr1[i][0] ^ arr1[i][1]) for i in range(0,len(arr1))]
    print(arr2)
    xor=arr2[0]
    arr3=[(arr2[i][0] ^ arr2[i][1]) for i in range(0,len(arr2))]
    print(arr3)
else:
    arr1=[(arr[i],arr[i+1]) for i in range(0,len(arr)-1,2)]
    arr1.append(arr[-1])

print(arr1)