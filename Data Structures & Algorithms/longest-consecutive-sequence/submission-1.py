class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        valid_start = []
        for n in nums:
            if n-1 not in numset:
                valid_start.append(n)
        
        max_len = 0
        for start in valid_start:
            curr = start
            len = 0
            while True:
                if curr in numset:
                    len += 1
                    curr += 1 
                else:
                    break
            if len > max_len:
                max_len = len

        return max_len