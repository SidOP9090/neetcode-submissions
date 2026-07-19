class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        output = 0
        for i in range(len(heights)):
            l = i
            r = i
            while True:
                if l == 0:
                    break
                else:
                    if heights[l-1] >= heights[i]:
                        l -= 1
                    else:
                        break
            while True:
                if r == len(heights)-1:
                    break
                else:
                    if heights[r+1] >= heights[i]:
                        r += 1
                    else:
                        break
               
            width = r-l+1
            output = max(output,heights[i]*width)
        return output



            
        


        

        