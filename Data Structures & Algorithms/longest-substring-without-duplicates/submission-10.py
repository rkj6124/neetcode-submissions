class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        i, j = 0, 1
        stack = set()
        stack.add(s[i])
        maxlen = 0
        while i < len(s) and j < len(s):
            while s[j] in stack:
                    stack.discard(s[i])
                    i += 1
            stack.add(s[j])
            j += 1
            if len(stack) > maxlen:
                    maxlen = len(stack)

        return maxlen
