#https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
count=0
def numberOfSteps(num):
    global count
    print(num)
    if num<1:
        print("count",count)
        return count
    if num%2==0:
        num=num//2
        count+=1
    else:
        num=(num-1)
        count+=1
    return numberOfSteps(num)

print(numberOfSteps(123))

#accepted