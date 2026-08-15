class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        while left < right:
            if left_max < right_max:
                left += 1
                if left_max < height[left]:
                    left_max = height[left]
                total_water += left_max - height[left]

            else:
                right -=1 
                if right_max < height[right]:
                    right_max = height[right]
                total_water += right_max - height[right]
        return total_water
