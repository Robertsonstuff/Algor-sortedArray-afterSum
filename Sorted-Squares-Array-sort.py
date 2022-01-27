# O(nlog(n)) time, O(n)space

def sortedSquaresArray(array):
    sortedSquares = [0 for _ in array]
    # this creates a list named sorted squares with values of '0'. In this case it's the length of the array which is [0,0,0,0,0,0,0]
    
    for idx in range(len(array)):
        value = array[idx]
        sortedSquares[idx] = value * value
        # print(sortedSquares) if you uncomment this algorithm, you'll see it at work.

    sortedSquares.sort()
    return sortedSquares
# this for loop sets up the index of the array named "value". 
# the value is then times by itself (9*9) and put in to the list created in (line4)
# once it has looped through the array is will call the inbuilt function .sort() to sort the list sortedsquares from smallest to largest. 

result = sortedSquaresArray([9,1,2,6,8,3,5])
print(result)