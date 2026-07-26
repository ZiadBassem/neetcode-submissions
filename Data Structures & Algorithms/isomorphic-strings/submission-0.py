class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapt = {}
        maps = {}
        for i in range(len(s)):
            c1,c2 = s[i],t[i]
            if (c1 in mapt and mapt[c1] != c2) or (c2 in maps and maps[c2] != c1):
                return False
            mapt[c1] = c2
            maps[c2] = c1
        return True
        