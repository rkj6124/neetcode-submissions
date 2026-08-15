class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        smap = dict.fromkeys(s, 0)
        print(smap)
        for c in s: 
            smap[c] += 1
        print(smap)
        for c in t:
            if c not in smap:
                return False
            smap[c] -= 1
        for _, val in smap.items():
            if val > 0 or val < 0:
                return False
        return True