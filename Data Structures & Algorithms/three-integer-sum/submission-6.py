class Solution:
    def threeSum(self, nums1: List[int]) -> List[List[int]]:
        output = []
        nums = sorted(nums1)
        for i in range(len(nums1)):
            target = -nums[i]
            l,r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r]< target:
                    l += 1 
                elif nums[l] + nums[r] == target:
                    output.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
        output_main = []
        for triplet in output:
            triplet.sort()
            if triplet not in output_main:
                output_main.append(triplet)
        return output_main
            
                    


        