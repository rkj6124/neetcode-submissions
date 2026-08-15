class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            target = 0 - nums[i]
            twoSumResList = self.twoSum(target, nums, i)
            for pair in twoSumResList:
                triplet = sorted(pair + [nums[i]])
                res.add(tuple(triplet))
        return [list(li) for li in res]


    def twoSum(self, target: int, nums: List[int], skipIdx: int) -> List[List[int]]:
        left = 0
        right = len(nums) - 1
        results = []

        while left < right:
            if left == skipIdx:
                left += 1
                continue
            if right == skipIdx:
                right -= 1
                continue
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                results.append([nums[left], nums[right]])
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return results