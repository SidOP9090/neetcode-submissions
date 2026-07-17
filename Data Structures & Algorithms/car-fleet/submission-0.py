class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = []
        for i,j in zip(position,speed):
            car.append([i,j])
        car.sort(reverse=True)
        stack = []
        for p,s in car:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
            

\

        
    
    
    
    

            

        


        
        