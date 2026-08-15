class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueNum = set(nums)
        if len(uniqueNum) != len(nums):
            return True
        return False