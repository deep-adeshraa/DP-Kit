"""
0-1 Knapsack problem

You are given weights and values of N items, put these items in a knapsack of 
capacity W to get the maximum total value in the knapsack. Note that we have 
only one quantity of each item.
In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which 
represent values and weights associated with N items respectively. Also given 
an integer W which represents knapsack capacity, find out the maximum value 
subset of val[] such that sum of the weights of this subset is smaller than or 
equal to W. You cannot break an item, either pick the complete item, or don’t 
pick it (0-1 property).

Example 1:

Input:
N = 3
W = 4
values[] = {1,2,3}
weight[] = {4,5,1}
Output: 3

Example 2:

Input:
N = 3
W = 3
values[] = {1,2,3}
weight[] = {4,5,6}
Output: 0
"""


def knapsack_recurse(C, wt, val, n, memo={}):
    '''
    Code with memoization(Bottom up approach).

    :param C: capacity of knapsack 
    :param wt: list containing weights
    :param val: list containing corresponding values
    :param n: size of lists
    :return: Integer
    '''
    if C == 0 or n == 0:
        return 0

    key = (n, C)

    if memo.get(key) is not None:
        return memo[key]

    if wt[n-1] <= C:
        val = max(val[n-1] + knapsack_recurse(C-wt[n-1], wt, val, n-1, memo),
                  knapsack_recurse(C, wt, val, n-1, memo))
    else:
        val = knapsack_recurse(C, wt, val, n-1, memo)

    memo[key] = val

    return val


def knapsack_dp(C, wt, val, n):
    K = [[0 for x in range(C + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(C + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][C]
