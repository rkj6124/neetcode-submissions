class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i, num in enumerate(nums):
            num_to_search = target - num
            if num_to_search in num_dict:
                return [num_dict[num_to_search], i]
            else:
                num_dict[num] = i

        