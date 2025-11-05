#set kavramını araştırdım 
class Solution(object):
    def isValidSudoku(self, board):
        
        row = [set() for _ in range(9)]
        column = [set() for _ in range(9)]        
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                
                if(value == '.'):
                    continue
                
                box_index = (r/3) * 3 + (c/3)
                
                if(value in row[r]):
                    return False
                
                if(value in column[c]):
                    return False
                
                if(value in boxes[box_index]):
                    return False
                
                row[r].add(value)
                column[c].add(value)
                boxes[box_index].add(value)   
        
        return True     
        
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        