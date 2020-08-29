#   1   2   3   4
        #   1   1   2   6
        #   24  12  8   6
        p = 1
        output = []
        for i in range(0,len(nums)):
            output.append(p)
            p *= nums[i]
        p = 1
        for i in range(len(nums) - 1,-1,-1):
            output[i] = output[i] * p
            p *= nums[i]
        return output
        
        
        
