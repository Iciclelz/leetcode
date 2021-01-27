class Solution:
    def __init__(self):
        self.solution = list()
        
    def branch(self, nums, subset, curr):
        if curr == len(nums):
            if subset != None:
                self.solution.append(list(filter(lambda x : x is not None, subset)))
            return
        
        i, j = subset.copy(), subset.copy()
        i[curr], j[curr] = None, nums[curr]
        self.branch(nums, i, curr + 1)
        self.branch(nums, j, curr + 1)
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.branch(nums, nums, 0)
        return self.solution