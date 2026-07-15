class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for n in numbers:
            numbers_1 = numbers.copy()
            numbers_1.remove(n)
            if target - n in numbers_1:
                return [numbers.index(min(n,target-n))+1,numbers.index(max(n,target-n))+1]
        return []

        