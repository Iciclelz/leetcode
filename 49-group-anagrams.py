class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for s in strs:
            val = ''.join(sorted(list(s)))
            if val in d:
                d[val].append(s)
            else:
                d[val] = [s]
        return list(d.values())
                