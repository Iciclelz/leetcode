class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.strip().split(' ')
        return len(l[len(l) - 1])