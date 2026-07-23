class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j = 0
        merge_sort_array = []
        while i <=len(nums1)-1 and j <= len(nums2)-1:
            if nums1[i]<=nums2[j]:
                merge_sort_array.append(nums1[i])
                i +=1
            else:
                merge_sort_array.append(nums2[j])
                j += 1
        print(i)
        print(j)
        if i != len(nums1):
            for a in range(i,len(nums1)):
                merge_sort_array.append(nums1[a])
        elif j != len(nums2):
            for b in range(j,len(nums2)):
                merge_sort_array.append(nums2[b])

        print(merge_sort_array)
        if len(merge_sort_array)%2 ==0:
            return (merge_sort_array[len(merge_sort_array)//2] + merge_sort_array[len(merge_sort_array)//2-1])/2
        else:
            return merge_sort_array[len(merge_sort_array)//2]
            
            


        