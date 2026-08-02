# Dynamic Programming - Fibonacci
# Using Memoization and Tabulation

# Memoization Method
def fibonacci_memo(n, memo=None):

    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# Tabulation Method
def fibonacci_tab(n):

    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Main Program
num = int(input("Enter Fibonacci Position: "))

print("\nResult using Memoization :", fibonacci_memo(num))
print("Result using Tabulation  :", fibonacci_tab(num))

"""
Enter Fibonacci Position: 3

Result using Memoization : 2
Result using Tabulation  : 2
"""