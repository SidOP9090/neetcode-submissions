class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][0])
        low = 0
        high = len(row)-1
        row_search = 0
        if target>row[-1]:
            row_search = len(row)-1
        else:
            while low<=high:
                middle = (low+high)//2
                if target == row[middle]:
                    return True
                elif target < row[middle]:
                    high = middle-1
                elif target > row[middle]:
                    low = middle + 1
            row_search = high
        low = 0
        high = len(matrix[row_search])-1
        while low<=high:
            middle = (low+high)//2
            if target == matrix[row_search][middle]:
                return True
            elif target>matrix[row_search][middle]:
                low = middle+1
            elif target<matrix[row_search][middle]:
                high = middle-1
        return False
    











        

        

        
        
        