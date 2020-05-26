class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = max(nums) #O(n)
        v = list(range(len(nums) + 1))
        return sum(v) - sum(nums)
            