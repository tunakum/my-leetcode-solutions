class Solution(object):
    def searchMatrix(self, matrix, target):
        left = 0
        right = len(matrix) - 1
        
        while(left <= right):
            mid_row = (left + right) // 2
            
            if(matrix[mid_row][0] <= target <= matrix[mid_row][-1]):
                
                l = 0
                r = len(matrix[mid_row]) - 1
                
                while(l <= r):
                    mid_column = (l + r) // 2
                    
                    if(matrix[mid_row][mid_column] == target):
                        return True
                    elif(matrix[mid_row][mid_column] < target):
                        l = mid_column + 1
                    else:
                        r = mid_column - 1
                return False

            elif(target < matrix[mid_row][0]):
                right = mid_row - 1
            else:
                left = mid_row + 1
        return False
        
        
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        