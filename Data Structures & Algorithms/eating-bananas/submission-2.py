class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        # answer must lie between l and r
        res = len(piles)

        if len(piles) == h:
            return max(piles)
        while l <= r:
            k = (l + r) // 2
            time = sum([(p // k) + 1 if p % k != 0 else p // k for p in piles])
            if time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res

