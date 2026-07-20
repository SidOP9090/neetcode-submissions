class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        left = []
        right = []
        for i in range(len(heights)):
            if not stack:
                stack.append(i)
                left.append(-1)
            elif stack:
                while heights[i]<=heights[stack[-1]]:
                    stack.pop()
                    if not stack:
                        break
                if not stack:
                    left.append(-1)
                else:
                    left.append(stack[-1])
                stack.append(i) 
        stack = []
        n = len(heights)-1                                                                                     
        for j in range(len(heights)):
            if not stack:
                stack.append(n-j)
                right.append(len(heights))
            elif stack:
                while heights[n-j]<=heights[stack[-1]]:
                    stack.pop()
                    if not stack:
                        break
                if not stack:
                    right.append(len(heights))
                else:
                    right.append(stack[-1])
                stack.append(n-j)
        right.reverse()            
        output = 0
        for l,r,v in zip(left,right,heights):
            width = r-l-1
            area = v*width
            output = max(output,area)
        return output

        