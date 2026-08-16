class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        res = []
        stack = []
        for i in range(l-1, -1, -1):
            if not stack:
                res.append(0)
            elif temperatures[stack[-1]] > temperatures[i]:
                res.append(stack[-1]-i)
            elif temperatures[stack[-1]] <= temperatures[i]:
                while stack and temperatures[stack[-1]] <= temperatures[i]:
                    stack.pop()

                if not stack:
                    res.append(0)
                else:
                    res.append(stack[-1]-i)
            stack.append(i)
        return res[::-1]
