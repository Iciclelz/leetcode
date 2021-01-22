class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = False
        
        digits[len(digits) - 1] += 1
        for x in range(len(digits) - 1, -1, -1):
            if digits[x] == 10:
                digits[x] = 0
                if x-1 < 0:
                    a = True
                else:
                    digits[x-1] += 1
        if a:
            digits.insert(0, 1)
        
        return digits