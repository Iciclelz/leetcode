class NumArray:

    def __init__(self, nums: List[int]):
        self.cache = list()
        self.cache = nums
        for x in range(1, len(nums)):
            self.cache[x] = self.cache[x-1] + nums[x]

    def sumRange(self, i: int, j: int) -> int:
        return self.cache[j] if i == 0 else self.cache[j] - self.cache[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)