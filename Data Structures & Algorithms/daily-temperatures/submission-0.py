class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = 0
        output = []
        for i in range(len(temperatures)):
            count = 0
            inn = 0
            for j in range(l,len(temperatures)):
                if temperatures[j]>temperatures[l]:
                    l +=1
                    inn += 1
                    output.append(count)
                    break
                else:
                    count +=1
            if inn == 0:
                output.append(0)
                l += 1
        return output

            
        


        
        

