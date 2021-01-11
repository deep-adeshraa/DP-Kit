"""
Count of subsets with sum equal to X

Given an array arr[] of length N and an integer X, the task is to find the number of subsets with sum equal to X.

Examples:

Input: arr[] = {1, 2, 3, 3}, X = 6
Output: 3
All the possible subsets are {1, 2, 3},
{1, 2, 3} and {3, 3}

Input: arr[] = {1, 1, 1, 1}, X = 1
Output: 4

"""


class Solution:

    def recurse(self, nums, sum, n, curr_sum, curr_ptr):

        # Base cases
        if sum == curr_sum:
            return n+1

        if curr_ptr > len(nums)-1:
            return n

        # 2 choices
        include = self.recurse(nums, sum, n, curr_sum +
                               nums[curr_ptr], curr_ptr+1)
        not_include = self.recurse(nums, sum, n, curr_sum, curr_ptr+1)

        return include + not_include

    def dp(self, nums, sum):
        # sum * nums matrix
        # # `Remember to create 1 column more than sum`
        matrix = [[0 for i in range(sum+1)] for i in nums]

        # Base cases
        for i in range(len(nums)):
            matrix[i][0] = 1

        for i in range(1, sum+1):
            matrix[0][i] = 0
            if nums[0] == i:
                matrix[0][i] = 1

        # Fill the dp table
        for i in range(1, len(nums)):
            for curr_sum in range(1, sum+1):

                if curr_sum < nums[i]:
                    matrix[i][curr_sum] = matrix[i-1][curr_sum]

                else:
                    matrix[i][curr_sum] = matrix[i-1][curr_sum] + \
                        matrix[i-1][curr_sum-nums[i]]

        return matrix[-1][-1]


if __name__ == "__main__":
    sol = Solution()

    nums = [1, 5, 3, 2, 4, 1, 1, 1]
    sum = 5

    re_count = sol.recurse(nums, sum, 0, 0, 0)
    print(re_count)

    dp_count = sol.dp(nums, sum)
    print(dp_count)

    print("-----------", re_count == dp_count, "-----------")
