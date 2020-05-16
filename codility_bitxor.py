# def solution1(M, N):
#     # write your code in Python 3.6
#     xor=0
#     if M<N:
#         for i in range(M,N+1):
#             xor=xor^i
#             print(xor)
#     return xor
# def solution2(M, N):
#     # write your code in Python 3.6
    
#     arr=[(i,i+1) for i in range(M,N+1,2)]
#     print(arr)
#     xor_arr=[]
#     xor_sum=0
#     for i in range(len(arr)):
#         xor_sum=arr[i][0]^arr[i][1]
#         print(arr[i][0],arr[i][1])
#         (xor_arr.append(xor_sum))
#     print(xor_arr)
#     arr_xor=[(xor_arr[i],xor_arr[i+1]) for i in range(0,len(xor_arr),2)]
#     print(arr_xor)
#     for i in range(len(arr_xor)):
#         xor_sum=arr_xor[i][0]^arr_xor[i][1]
#     print(xor_sum)

    
#     # if M<N:
#     #     for i in range(0,len(arr),2):
#     #         #print("i",i)
#     #         #xor=xor^arr[i]^arr[i+1]
#     #         #print(xor)
#     #         ...
#     # return xor
# def xor_op(a,b):
#     return xor_op(a,b)

# def main(a,b):
#     if a<0 or b<0:
#         return
    
# def solution(M,N):
#     arr=[i for i in range(M,N+1)]
#     result=main(arr[0],arr[-1])
#     return result


# #print(solution(5,8)) #12
# print(solution(12,21)) #25
        
def printPatternRowRecur(n): 
  
    # base condition 
    if (n < 1): 
        return
          
    # print the remnaining  
    # stars of the n-th row 
    # recursively  
    print("*", end = " ") 
    print(n[0]^n[1])
    printPatternRowRecur(n - 1) 
  
def printPatternRecur(n): 
  
    # base condition 
    if (n < 1): 
        return
      
    # print the stars of 
    # the n-th row  
    printPatternRowRecur(n)  
      
    # move to next line 
    print("") 
      
    # print stars of the  
    # remaining rows recursively 
    printPatternRecur(n - 1) 
      
# Driver Code 
n = 5
printPatternRecur(n)