class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # num_dict = dict.fromkeys(nums, [])
        num_dict = {}

        for i, num in enumerate(nums):
            if num in num_dict:
                num_dict[num].append(i)
            else:
                num_dict[num] = [i]

        print(num_dict)

        for i, num in enumerate(nums):
            num_to_search = target - num
            print(f"num: {num}")
            print(f"num_to_search: {num_to_search}")
            if num_to_search not in num_dict:
                continue
            print(f"search_indx: {num_dict[num_to_search]}")
            for j in num_dict[num_to_search]:
                if i != j:
                    tgt_index = j
                    return [tgt_index, i] if i > tgt_index else [i, tgt_index]

        