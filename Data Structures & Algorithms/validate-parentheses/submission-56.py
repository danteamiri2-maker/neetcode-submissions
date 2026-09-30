class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']':'[', '}': '{'}
        stack = []

        i = 0
        valid = True if len(s)%2==0 else False
        while i < len(s) and valid:
            c = s[i]
            
            if c not in pairs.keys():
                stack.append(c)

            if c in pairs.keys():
                if len(stack) == 0:
                    return False
                
                if pairs[c] != stack.pop():
                    return False

            i += 1
        
        return valid and len(stack) == 0
            




