class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        seen = dict()

        for s in strs:
            char_freq = dict()
            sorted_s = sorted(list(s))
            for c in sorted_s:
                if c in char_freq:
                    char_freq[c] += 1
                if c not in char_freq:
                    char_freq[c] = 1

            code = ''.join([c + str(val) for c, val in char_freq.items()])

            if code in seen:
                anagrams[seen[code]].append(s)

            if code not in seen:
                anagrams.append([s])
                seen[code] = len(anagrams)-1
            
        return anagrams