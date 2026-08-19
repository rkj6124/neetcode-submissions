class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            if nums[r] > nums[l]:
                return min(res, nums[l])
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                # we are in left side and we should aim to search in the right
                # because in right we will find the minimum since rotated
                l = m + 1
            else:
                r = m - 1
        return res