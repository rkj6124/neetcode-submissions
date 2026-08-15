class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_map = {}
        contains_duplicate = False
        for n in nums:
            if freq_map.get(n):
                if freq_map[n] == 1:
                    contains_duplicate = True
                    break
                freq_map[n] += 1
            else:
                freq_map[n] = 1
        return contains_duplicate