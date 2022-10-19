"""
Given a value V, if we want to make a change for V cents, and we have an
infinite supply of each of C = { C1, C2, .., Cm} valued coins, what is the
minimum number of coins to make the change? If it's not possible to make a
change, print -1.

Examples:

Input: coins[] = {25, 10, 5}, V = 30
Output: Minimum 2 coins required
We can use one coin of 25 cents and one of 5 cents

Input: coins[] = {9, 6, 5, 1}, V = 11
Output: Minimum 2 coins required
We can use one coin of 6 cents and 1 coin of 5 cents
"""


def min_coins(allowed_coins, value, index):
    if value == 0:
        return 0

    if index == len(allowed_coins):
        return float('inf')

    ans = 0

    if value >= allowed_coins[index]:
        ans = min(1 + min_coins(allowed_coins, value - allowed_coins[index], index),
                  min_coins(allowed_coins, value, index+1))
    else:
        ans = min_coins(allowed_coins, value, index+1)

    return ans


coins = [25, 10, 1]
value = 85
ans = min_coins(coins, value, 0)
print("min coins ", ans)


def num_ways(items, value, n=0):
    if value == 0:
        return 1

    if value < 0:
        return 0

    if n == len(items):
        return 0

    return num_ways(items, value - items[n], n) + num_ways(items, value, n+1)


print("num of ways", num_ways(coins, value))
