# 🔹 Problem
# You’re given an array cost where:
# cost[i] = cost of stepping on stair i
# You can start from step 0 or step 1
# Each move: climb 1 or 2 steps
# You must reach just beyond the last step (n)
# 👉 Return the minimum cost to reach the top.

# Key Shift from Problem 2

# Problem 2 was:
# “How many ways?”
# Problem 3 is:
# “What is the minimum cost?”
# Same movement rules.
# Different DP meaning.

# 1️⃣ Define the DP State (MOST IMPORTANT)
# dp[i] = minimum cost to reach step i
# ⚠️ Step i means you are standing on it, and you pay cost[i] when you step on it.

# 2️⃣ Transitions (Why this works)
# To reach step i:
# You came from i-1
# Or from i-2
# So:
# dp[i] = cost[i] + min(dp[i-1], dp[i-2])
# You pay:
# the cost of this step
# plus the minimum cost to reach one of the previous valid steps


# 3️⃣ Base Cases (Very Important)
# dp[0] = cost[0]
# dp[1] = cost[1]

# Why?
# You can start directly at step 0 or 1
# You pay the cost when stepping on it
# 4️⃣ Final Answer (Common Confusion)
# You do NOT pay for the top (step n).
# So answer is:
# min(dp[n-1], dp[n-2])
# Because:
# You can reach the top from either of the last two steps

# 🧩 Example
# cost = [10, 15, 20]

# DP table:
# dp[0] = 10
# dp[1] = 15
# dp[2] = 20 + min(10, 15) = 30


# Answer:
# min(dp[1], dp[2]) = min(15, 30) = 15
# ✍️ Your Task
# Implement DP array solution
# Then try space optimized
# Test with:

# [10,15,20]       → 15
# [1,100,1,1,1]   → 3

# ⚠️ Very Common Mistake
# ❌ Adding cost at the wrong time
# ❌ Returning dp[n]
# ❌ Misunderstanding what step you’re paying for

# 🧠 DP Pattern You Just Learned
# Min / Max DP with choices
# This exact pattern appears in:
# Stock buy/sell
# Scheduling
# Path cost problems


def min_cost_climbing_stairs(cost):
    n = len(cost)
    dp = [0] * n

    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])

    return min(dp[n-1], dp[n-2])

# Space Optimised
def min_cost_climbing_stairs(cost):
    prev2 = cost[0]
    prev1 = cost[1]

    for i in range(2, len(cost)):
        curr = cost[i] + min(prev1, prev2)
        prev2, prev1 = prev1, curr

    return min(prev1, prev2)
