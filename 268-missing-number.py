class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(max(nums) + 1)) - sum(nums)