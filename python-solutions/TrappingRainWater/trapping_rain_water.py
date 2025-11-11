#The first solution was logically correct but caused a Time Limit Exceeded
#class Solution(object):
#def trap(self, height):
#n = len(height)
#total_water = 0

# for i in range(n):
#      left_max = max(height[:i+1])
#       
#        right_max = max(height[i:])
#         
#          total_water += min(left_max, right_max) - height[i]
#       
#        return total_water
            
# I used a similar solution before when solving the "container with most water" problem,
# so I used that as a cheatsheet for this one.
class Solution(object):
    def trap(self, height):
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        total_water = 0
        
        while(left < right):
            if(height[left] < height[right]):
                if(height[left] >= left_max):
                    left_max = height[left]            
                else:
                    total_water += left_max - height[left]
                left += 1
            else:
                if(height[right] >= right_max):
                    right_max = height[right]
                else:
                    total_water += right_max - height[right]
                right -= 1
        return total_water
        
        """
        :type height: List[int]
        :rtype: int
        """
        