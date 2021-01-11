"""
Partition Equal Subset Sum

Given a non-empty array nums containing only positive integers, 
find if the array can be partitioned into two subsets such that the sum of
elements in both subsets is equal.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""


class Solution(object):

    def dp(self):
        # TODO
        pass

    def recurse(self, p1, p2, nums, n):

        if p1 == p2 and n == len(nums):
            return True

        if n >= len(nums):
            return False

        add_in_p1 = self.recurse(p1 + nums[n], p2, nums, n+1)
        add_in_p2 = self.recurse(p1, p2+nums[n], nums, n+1)

        return add_in_p1 or add_in_p2

    def dp(self, nums):
        Sum = sum(nums)
        max_elem = max(nums)

        if Sum % 2 == 1:
            return False

        if max_elem > Sum // 2:
            return False

        target = Sum // 2
        # Now this has became subset sum problem (how ?)

        matrix = [[False for i in range(target+1)] for i in range(len(nums))]

        for i in range(len(nums)):
            for j in range(target+1):
                # here j is curr_sum
                if i == 0:
                    matrix[i][j] = False
                elif j == 0:
                    matrix[i][j] = True
                elif j < nums[i]:
                    matrix[i][j] = matrix[i-1][j]
                else:
                    matrix[i][j] = matrix[i-1][j] or matrix[i-1][j-nums[i]]

        return matrix[-1][-1]

    def canPartition(self, nums):
        p1, p2 = 0, 0
        ans = self.recurse(p1, p2, nums, 0)

        return ans


if __name__ == "__main__":
    solution = Solution()
    ans = solution.canPartition([1, 5])  # [4 3 2 - 1 4 4]

    print(ans)
