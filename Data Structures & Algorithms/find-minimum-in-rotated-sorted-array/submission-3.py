class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        minimum = None
        if nums[l]<nums[r]:
            return nums[0]
        else:
            while l<=r:
                middle = (l+r)//2
                if nums[l]<=nums[middle]:
                    if minimum is None:
                        minimum = nums[l]
                    else:    
                        minimum = min(minimum,nums[l])
                    l = middle + 1
                elif nums[middle]<=nums[r]:
                    if minimum is None:
                        minimum = nums[middle]
                    else:    
                        minimum = min(minimum,nums[middle])
                    r = middle-1
                elif nus[l]<nums[r]:
                    minimum = min(minimum,nums[l])
                    break
        return minimum
            



                    










