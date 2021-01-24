class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = dict()
        
        for n in range(len(s)):
            if s[n] in m:
                m[s[n]] += 1
            else:
                m[s[n]] = 1
        
        if len(m.keys()) == 0:
            return -1;
        
        for n in range(len(s)):
            if m[s[n]] == 1:
                return n
        
        return -1