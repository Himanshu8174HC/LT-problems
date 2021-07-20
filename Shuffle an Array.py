class Solution:

    def __init__(self, nums: List[int]):
        
        self.nums = nums
        

    def reset(self) -> List[int]:
       
        return list(self.nums)
        

    def shuffle(self) -> List[int]:
        
        nums = list(self.nums)
        temp = []
        k = len(nums)-1
        
        for i in range(k+1):
            j = random.randint( 0 , k-i)
            nums[j] , nums[-1] = nums[-1], nums[j]
            temp.append(nums.pop())
        return temp
