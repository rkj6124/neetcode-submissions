class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod_from_start = [] 
        prod_from_end = []
        prod = 1
        for num in nums:
            prod = prod * num
            prod_from_start.append(prod)
        print(prod_from_start)
        prod = 1
        for num in nums[::-1]:
            prod = prod * num
            prod_from_end.append(prod)
        prod_from_end = prod_from_end[::-1]
        print(prod_from_end) 
        res = [1] * len(nums)
        for i, val in enumerate(res):
            if i == 0:
                prev = 1
            else:
                prev = prod_from_start[i-1]
            if i == len(nums) - 1:
                after = 1
            else:
                after = prod_from_end[i+1]
            res[i] = prev * after
        return res



       