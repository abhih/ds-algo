def rec_possible_keyword(var, curr=0,output=[]):
    if curr==n:
        #print(output)
        return
    print(keypad[var[curr]])
    
    return rec_possible_keyword(var,curr=curr+1)
    

#todo

keypad=[[],[],
        [ 'A', 'B', 'C' ],#2
        [ 'D', 'E', 'F' ],#3
		[ 'G', 'H', 'I' ],#4
		[ 'J', 'K', 'L' ],#5
		[ 'M', 'N', 'O' ],#6
		[ 'P', 'Q', 'R', 'S'], #7
		[ 'T', 'U', 'V' ],#8
		[ 'W', 'X', 'Y', 'Z']#9
        ]

input_=[2,3,4]
n=len(input_)
print(rec_possible_keyword(input_))