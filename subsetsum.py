"""
Subset Sum Problem

Given a set of non-negative integers, and a value sum, determine if there is a 
subset of the given set with sum equal to given sum. 

Example: 

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True  
There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
There is no subset that add up to 30.
"""

class Solution:

    def recurse(self, nums, sum, i):
        if sum == 0:
            return True
        
        if i>=len(nums):
            return sum == 0
        
        include = self.recurse(nums, sum-nums[i], i+1)
        not_include = self.recurse(nums, sum, i+1)

        return include or not_include

    def dp(self, nums, sum):
        matrix = [[False for i in range(sum+1)] for i in range(len(nums))]

        # Remember : Fill first row and column
        for i in range(sum+1):
            matrix[0][i] = False
        
        for i in range(len(nums)):
            matrix[i][0] = True
        
        for num in range(1, len(nums)):
            for curr_sum in range(1, sum+1):
                if curr_sum < nums[num]:
                    matrix[num][curr_sum] = matrix[num-1][curr_sum] # not include
                
                elif curr_sum >= nums[num]:
                    matrix[num][curr_sum] = (matrix[num-1][curr_sum-nums[num]] or # Include case
                                             matrix[num-1][curr_sum]) # Not include case

        return matrix[-1][-1]

if __name__ == "__main__":
    
    sol = Solution()

    nums = [3, 34, 4, 12, 5, 2]
    sum = 38

    is_possible = sol.recurse(nums, sum, 0)
    is_possible = sol.dp(nums, sum)
    print(is_possible)

