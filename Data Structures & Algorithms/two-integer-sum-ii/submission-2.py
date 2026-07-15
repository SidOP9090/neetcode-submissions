class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for n in numbers:
            if target - n in numbers:
                if numbers.index(target-n) == numbers.index(n):
                    continue
                return [numbers.index(min(n,target-n))+1,numbers.index(max(n,target-n))+1]
        return []

        