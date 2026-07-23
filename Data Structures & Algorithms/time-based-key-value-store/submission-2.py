from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        low = 0
        high = len(self.timeMap[key])-1
        if timestamp < self.timeMap[key][low][0]:
            return ""
        elif timestamp > self.timeMap[key][high][0]:
            return self.timeMap[key][high][1]
        while low<= high:
            mid = (low+high)//2
            if timestamp == self.timeMap[key][mid][0]:
                return self.timeMap[key][mid][1]
            elif timestamp>self.timeMap[key][mid][0]:
                low = mid+1
            else:
                high = mid -1
        return self.timeMap[key][high][1]
        
                

                

        
