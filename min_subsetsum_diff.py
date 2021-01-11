"""
Partition a set into two subsets such that the difference of subset sums is
minimum

Given a set of integers, the task is to divide it into two sets S1 and S2 such 
that the absolute difference between their sums is minimum. 
If there is a set S with n elements, then if we assume Subset1 has m elements,
Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2))
should be minimum.

Example:
Input:  arr[] = {1, 6, 11, 5}
Output: 1

Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12
Subset2 = {11}, sum of Subset2 = 11
"""
import datetime


class Solution:

    def __init__(self):
        self.memo = {}

    def recurse(self, nums, n, a_sum, b_sum):

        if n >= len(nums):
            return abs(a_sum - b_sum)

        in_a = self.recurse(nums, n+1, a_sum+nums[n], b_sum)
        in_b = self.recurse(nums, n+1, a_sum, b_sum+nums[n])

        ans = min(in_a, in_b)

        return ans

    def memoization(self, nums, n, a_sum, b_sum):
        if n >= len(nums):
            return abs(a_sum - b_sum)

        key = (nums[n], abs(a_sum-b_sum))

        if (self.memo.get(key) is not None):
            return self.memo[key]

        in_a = self.memoization(nums, n+1, a_sum+nums[n], b_sum)
        in_b = self.memoization(nums, n+1, a_sum, b_sum+nums[n])

        ans = min(in_a, in_b)

        self.memo[key] = ans

        return ans

    def dp(self, args):
        # TODO 
        pass


if __name__ == "__main__":
    sol = Solution()

    nums = [1, 2, 3, 4, 5, 6, 112, 5, 5, 5, 5, 7, 8]  # 108
    now = datetime.datetime.now()
    ans = sol.recurse(nums, 0, 0, 0)
    print("ans=", ans, "| time taken=",datetime.datetime.now() - now)

    now = datetime.datetime.now()
    ans = sol.memoization(nums, 0, 0, 0)
    print("ans=",ans, "| time taken=", datetime.datetime.now() - now)
