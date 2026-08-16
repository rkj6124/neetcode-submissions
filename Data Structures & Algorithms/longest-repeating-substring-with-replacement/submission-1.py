class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # len_window - max_frequency <= k (to be valid window)
        freq = {}
        l, res = 0, 0
        maxfreq = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxfreq = max(maxfreq, freq[s[r]])
            while (r - l + 1) - maxfreq > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
        