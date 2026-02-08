# The Fibonacci sequence looks like this:
# 0, 1, 1, 2, 3, 5, 8, 13, ...

# Rule (that’s it!)
# Every number is the sum of the previous two numbers
# So:
# F(0) = 0
# F(1) = 1
# F(2) = 1 → 0 + 1
# F(3) = 2 → 1 + 1
# F(4) = 3 → 1 + 2

# Why Dynamic Programming (DP)?
# The problem with “thinking fresh” every time
# If you calculate Fibonacci again and again for the same values, you:
# Waste time
# Repeat work
# Slow things down
# Dynamic Programming simply means:
# “If I already solved something, I’ll remember it and reuse it.”

# That’s it. No magic.

def fibonacci(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

