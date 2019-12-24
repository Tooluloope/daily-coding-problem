def twosum(arr,k):
     #assuming the two digits are distinct in position
     #i.e arr = [10,20,5] and k = 20 arr[0]+arr[0] = 20 since the two sum are not distinctive positionally, this is invalid

    for i in range(len(arr)-1):
        
        if k - arr[i] in arr[i:]:
            return True
    return False

def twosum1(arr,k):
    #Trade time for space complexity

    diction = {}

    for i in arr:
        if i in diction:
            return True
        else:
            diction[k-i] = i

    return False


print(twosum1([10, 15, 3, 7] , 10))
    