class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        g_max = max(nums)
        if len(nums) < 3:
            return g_max
        
        max_num = g_max
        m = 0
        for x in range(len(nums)):
            if nums[x - m] == max_num:
                nums.pop(x - m)
                m += 1
                
        if len(nums) == 0:
            return g_max
        
        max_num = max(nums)
        m = 0
        for x in range(len(nums)):
            if nums[x - m] == max_num:
                nums.pop(x - m)
                m += 1
        
        if len(nums) == 0:
            return g_max
        
        return max(nums)