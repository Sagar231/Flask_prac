class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # from math import *
        temp = []
        for _ in range(len(matrix)):
            temp.extend(matrix[_])
        l = 0
        h = temp.index(temp[-1])
        
        while l<=h:
            mid = math.floor((l+h)/2)
            if temp[mid]==target:
                return True
            elif temp[mid]>target:
                h = mid-1
            else:
                l = mid+1
        return False
