class Solution:
    def isPalindrome(self, s: str) -> bool:
        parsed = "".join(char.lower() for char in s if char.isalnum())
        n = len(parsed)
        left = 0
        right = n-1
        while left < right:
            if parsed[left] != parsed[right]:
                return False
            left += 1
            right -= 1
        return True