class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            middle = (l+r)//2
            if nums[middle] == target:
                return middle
            elif nums[l]<=nums[middle]:
                if nums[l]<=target<nums[middle]:
                    low = l
                    high = middle-1
                    while low<=high:
                        mid = (low+high)//2
                        if target == nums[mid]:
                            return mid
                        elif target>nums[mid]:
                            low = mid + 1
                        elif target<nums[mid]:
                            high = mid -1
                    return -1
                else:
                    l = middle + 1
            else:
                if nums[middle]<target<=nums[r]:
                    low = middle+1
                    high = r
                    while low<=high:
                        mid = (low+high)//2
                        if target == nums[mid]:
                            return mid
                        elif target>nums[mid]:
                            low = mid + 1
                        elif target<nums[mid]:
                            high = mid -1 
                    return -1
                else:
                    r = middle-1   
        return -1

                    

                

        