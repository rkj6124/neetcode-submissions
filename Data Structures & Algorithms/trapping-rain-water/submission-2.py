class Solution:
    def trap(self, height: list[int]) -> int:
        stack = []
        total_water = 0
        
        for i in range(len(height)):
            # While the current bar is taller than the stack's top bar
            while stack and height[i] > height[stack[-1]]:
                mid = stack.pop()  # This is the bottom floor of the valley
                
                if not stack:
                    break  # No left wall exists to trap water
                    
                left = stack[-1]  # The new top is our left wall boundary
                
                # Calculate horizontal water layer
                bounded_height = min(height[left], height[i]) - height[mid]
                width = i - left - 1
                
                total_water += bounded_height * width
                
            stack.append(i)  # Always push the current index onto the stack
            
        return total_water
