#https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
def kidsWithCandies(candies, extraCandies):
    most=max(candies)
    for c in candies:
        if extraCandies+c>=most:
            print(True)
        else:
            print(False)


candies=[2,3,5,1,3]
extra = 3
kidsWithCandies(candies, extra)
        

