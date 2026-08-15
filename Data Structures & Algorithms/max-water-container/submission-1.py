class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        max_area = 0
        while left < right:
            lh = heights[left]
            rh = heights[right]
            w = right - left
            area = min(lh, rh) * w
            if area > max_area:
                max_area = area
            if lh < rh:
                left += 1
            else:
                right -= 1

        return max_area