from string import punctuation
class Solution:
    def isPalindrome(self, s: str) -> bool:

        
        translator = str.maketrans("", "", punctuation)
        s = s.translate(translator)
        s = s.lower()
        s = s.replace(" ", "")


        l, r = 0, len(s)-1  
        while l <= r:

            if s[l] != s[r]:
                return False

            l += 1
            r -= 1
        return True