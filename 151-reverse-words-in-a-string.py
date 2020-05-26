class Solution:
    def reverseWords(self, s: str) -> str:
        x = ' '.join(s.split(' ')[::-1]).strip()
        while '  ' in x:
            x = x.replace('  ', ' ')
        return x