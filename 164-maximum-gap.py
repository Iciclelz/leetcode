class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        nums.sort()        
        differences = list()
        
        for x in range(len(nums)-1):
            differences.append(nums[x+1] - nums[x])

        return max(differences)
        