class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l, r = 0, 0
        nums = []
        m, n = len(nums1), len(nums2)
        while l < m and r < n:
            f, s = nums1[l], nums2[r]
            if f < s:
                nums.append(f)
                l += 1
            else:
                nums.append(s)
                r += 1

        nums += nums1[l:]
        nums += nums2[r:]

        # print(l, r)
        # print(nums)
        return self.findmedian(nums)

    def findmedian(self, nums: List) -> float:
        l = len(nums)
        if l % 2 == 0:
            f = l // 2
            s = f - 1
            return (nums[f] + nums[s]) / 2
        else:
            i = (l + 1) // 2 - 1
            return nums[i]