class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        
        p = ''
        l = 0
        while l < min([len(s) for s in strs]):
            c = strs[0][l]
            for x in strs:
                if x[l] != c:
                    return p
            l += 1
            p += c
        return p
                