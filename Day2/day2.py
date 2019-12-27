def multiplyarr(arr):
    res = []
    left = []
    right = []
    start = 1
    end = 1
    for i in range(len(arr)-1):
        start *= arr[i]
        left.append(start)
    left.insert(0,1)
    for i in range(len(arr)-1, 0, -1):
        end *= arr[i]
        right.insert(0,end)
    right.append(1)

    for i in range(len(arr)):
        res.append(left[i] * right[i])
    return res


def multiply(arr):
# Accounts for zero elements

    res = [1 for i in range(len(arr))]
    mult = 1

    for i in range(len(arr)): 
        res[i] = mult 
        mult *= arr[i] 

  
    # Initialize mult to 1 for resuct on right side  
    mult = 1
  
    # In this loop, mult variable contains resuct of 
    # elements on right side excluding arr[i]  
    for i in range(len(arr) - 1, -1, -1): 
        res[i] *= mult 
        mult *= arr[i] 
    return res
        

print(multiply([1, 2, 3, 4, 0]))