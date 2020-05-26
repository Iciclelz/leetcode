class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for y in range(x):
                if nums[x] + nums[y] == target:
                    return [y, x]