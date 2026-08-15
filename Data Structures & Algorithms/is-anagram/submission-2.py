class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_map = {}
        for char in s:
            if freq_map.get(char):
                freq_map[char] += 1
            else:
                freq_map[char] = 1
        
        for char in t:
            if freq_map.get(char):
                if freq_map[char] == 0:
                    return False
                freq_map[char] -= 1
            else:
                return False
        
        for value in freq_map.values():
            if value != 0:
                return False

        return True