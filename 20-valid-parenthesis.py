class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = []

        for x in range(len(s)):
            
            if s[x] == '(' or s[x] == '[' or s[x] == '{':
                parenthesis.append(s[x])
          
            if s[x] == ')':
                if len(parenthesis) == 0 or parenthesis[-1] != '(':
                    return False
                
                parenthesis.pop()
            if s[x] == ']':
                if len(parenthesis) == 0 or parenthesis[-1] != '[':
                    return False
                
                parenthesis.pop()
            
            if s[x] == '}':
                if len(parenthesis) == 0 or parenthesis[-1] != '{':
                    return False
                
                parenthesis.pop()
            
        return len(parenthesis) == 0
        