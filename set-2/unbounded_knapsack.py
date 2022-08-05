"""
Unbounded Knapsack (Repetition of items allowed)

Given a knapsack weight W and a set of n items with certain value vali and 
weight wti, we need to calculate the maximum amount that could make up this 
quantity exactly. This is different from classical Knapsack problem, here we
are allowed to use unlimited number of instances of an item.

Examples: 
Input : W = 100
        val[]  = {1, 30}
        wt[] = {1, 50}
Output : 100

There are many ways to fill knapsack.
1) 2 instances of 50 unit weight item.
2) 100 instances of 1 unit weight item.
3) 1 instance of 50 unit weight item and 50
   instances of 1 unit weight items.
We get maximum value with option 2.

Input : W = 8
       val[] = {10, 40, 50, 70}
       wt[]  = {1, 3, 4, 5}       
Output : 110 
We get maximum value with one unit of
weight 5 and one unit of weight 3.
"""


class Solution:

    def recurse(self, capacity, val, weight, n):
        if capacity == 0 or n == len(val):
            return 0
        
        if weight[n] <= capacity:
            include = val[n] + self.recurse(capacity-weight[n], val, weight, n)
            exclude = self.recurse(capacity, val, weight, n+1)
            val = max(include, exclude)
        elif weight[n] > capacity:
            val = self.recurse(capacity, val, weight, n+1)

        return val

    def memoization(self, args):
        # TODO
        pass

    def dp(self, capacity, weight, value):
        dp = [0 for i in range(capacity + 1)]
        ans = 0

        # 1D dp
        for i in range(len(weight)):
            for j in range(capacity+1):
                if weight[i] <= j:
                    dp[j] = max(dp[j], value[i] + dp[j-weight[i]])
    
        return dp[capacity]
    
    def dp_2(self, capacity, weight, value):
        "DP in knapsack style"

        n = len(weight) + 1
        K = [[0 for i in range(capacity+1)] for i in range(n)]

        for i in range(n):
            for w in range(capacity + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif wt[i-1] <= w: #  change this -> K[i-1] -> K[i] in include.
                    K[i][w] = max(value[i-1] + K[i][w-wt[i-1]],
                                  K[i-1][w])
                else:
                    K[i][w] = K[i-1][w]
        
    
        return K[-1][-1]

if __name__ == "__main__":

    sol = Solution()
    capacity = 143
    val = [10, 40, 50, 70]
    wt = [1, 3, 4, 5]
    ans = sol.recurse(capacity, val, weight=wt, n=0)
    print(ans)
    ans = sol.dp_2(capacity, value=val, weight=wt)
    print(ans)
