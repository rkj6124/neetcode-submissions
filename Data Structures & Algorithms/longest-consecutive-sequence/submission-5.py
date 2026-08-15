class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numset = set(nums)
        max_len = 0

        for n in numset:
            if n - 1 not in numset:
                curr = n
                len = 1
            
                while True:
                    if curr + 1 in numset:
                        len += 1
                        curr += 1 
                    else:
                        break
            
                if len > max_len:
                    max_len = len

        return max_len