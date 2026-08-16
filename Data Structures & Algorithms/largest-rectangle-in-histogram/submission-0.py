class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # (nsr - nsl - 1) * h for each height, maximum one would be the answer
        # a building can expand only till it encounters nearest smaller on left or right
        n = len(heights)
        nsr = [n] * n
        nsl = [-1] * n

        nsrstack = []
        for i in range(n-1, -1, -1):
            while nsrstack and heights[nsrstack[-1]] >= heights[i]:
                nsrstack.pop()

            if nsrstack:
                nsr[i] = nsrstack[-1]
            
            nsrstack.append(i)

        nslstack = []
        for i in range(n):
            while nslstack and heights[nslstack[-1]] >= heights[i]:
                nslstack.pop()

            if nslstack:
                nsl[i] = nslstack[-1]

            nslstack.append(i)

        maxarea = 0
        pair = [(r - l - 1)*heights[i] for i, (r,l) in enumerate(zip(nsr, nsl))]
        return max(pair)
        