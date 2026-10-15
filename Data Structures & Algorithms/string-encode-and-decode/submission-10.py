class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, res = [], []
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res.append(str(sz))
            res.append(',')
        res.append('#')
        res.extend(strs)
        return ''.join(res)
        
        
    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        code_div = 0
        while s[code_div] != "#":
            code_div += 1

        pref = s[:code_div-1].split(",")

        suff = s[code_div+1:]

        strs = []
        k = 0
        for size in pref:
            size = int(size)
            strs.append(suff[k:k+size])
            k += size
        return strs


