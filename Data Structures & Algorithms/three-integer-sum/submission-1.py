class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            if nums[i] > 0:
                break

            target = 0 - nums[i]
            twoSumResList = self.twoSum(target, nums, i)
            for pair in twoSumResList:
                triplet = sorted(pair + [nums[i]])
                res.add(tuple(triplet))
        return [list(li) for li in res]


    def twoSum(self, target: int, nums: List[int], i: int) -> List[List[int]]:
        left = i + 1
        right = len(nums) - 1
        results = []

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                results.append([nums[left], nums[right]])
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            else:
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

        return results