def encode(arr):
    # Code here
    a = 1
    ans = ""
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            a += 1
        

        else:
            ans += arr[i] + str(a)
            a = 1
    ans += arr[len(arr)-1]+str(a)        
    return ans
