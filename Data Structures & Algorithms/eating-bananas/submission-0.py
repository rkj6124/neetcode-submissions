class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k):
            hours_needed = 0
            for pile in piles:
                hours_needed += (pile + k - 1) // k  # This is equivalent to ceil(pile / k)
            return hours_needed <= h
    
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if canFinish(mid):
                right = mid  # Try for a smaller speed
            else:
                left = mid + 1  # Increase speed
        
        return left

        