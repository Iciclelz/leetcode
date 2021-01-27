class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = nums[0]
        ct = 1
        for x in range(1, len(nums)):
            if ct == 0:
                n = nums[x]
                ct = 1
            else:
                ct += 1 if n == nums[x] else -1
        return n
'''
Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''