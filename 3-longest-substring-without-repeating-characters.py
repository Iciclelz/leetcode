class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        m = 1
        for _ in range(len(s)):
            i = 0
            S = set()
            for x in range(_, len(s)):
                if s[x] not in S:
                    S.add(s[x])
                    i += 1
                else:
                    break
            m = max(i, m)
            
        return m