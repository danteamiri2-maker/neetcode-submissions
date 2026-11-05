from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash1 = defaultdict(str)
        for c in s1:
            if c not in hash1:
                hash1[c] = 1
            
            else:
                hash1[c] += 1
            
        
        
        l = 0
        r = 0
        while r < len(s2):
            # add elements to window
            while r - l < len(s1) and r < len(s2):
                if s2[r] in hash1:
                    hash1[s2[r]] -= 1
                r += 1

            #print(hash1, l, r)
            if max(hash1.values()) == 0 and min(hash1.values()) == 0:
                return True

            if s2[l] in hash1:
                hash1[s2[l]] += 1
            l += 1
        
        return False
            
            