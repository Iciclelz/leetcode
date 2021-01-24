class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for n in range(1, len(nums)):
            nums[0] ^= nums[n]
        return nums[0]