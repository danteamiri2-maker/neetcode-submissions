class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        

        seen = dict()
        i = 0
        while i < len(s):
            print(s[i], t[i])
            if s[i] in seen:
                seen[s[i]] += 1
            
            if s[i] not in seen:
                seen[s[i]] = 1

            if t[i] in seen:
                seen[t[i]] -= 1

            if t[i] not in seen:
                seen[t[i]] = -1
            
            i += 1
        
        print(seen)
        if any(seen.values()):
            return False
        
        return True