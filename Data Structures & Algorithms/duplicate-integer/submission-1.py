class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = dict.fromkeys(nums, 0)
        for num in nums:
            map[num] += 1
        for key, val in map.items():
            if val > 1:
                return True
        return False
         