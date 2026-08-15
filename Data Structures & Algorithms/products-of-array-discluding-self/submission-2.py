class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_arr = [1] * n
        right_arr = [1] * n

        left_prod = 1
        for i in range(n):
            left_prod *= nums[i]
            left_arr[i] = left_prod

        right_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            right_prod *= nums[i]
            right_arr[i] = right_prod

        res = []

        for i in range(n):
            left = self.getVal(i-1, left_arr)
            right = self.getVal(i+1, right_arr)
            res.append(left * right)

        return res
            

    def getVal(self, i: int, arr: List[int]):
        if i < 0:
            return 1
        if i > len(arr)-1:
            return 1
        else:
            return arr[i]