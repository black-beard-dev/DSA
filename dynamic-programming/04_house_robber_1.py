# 📅 Problem 4 — House Robber
# You are a robber planning to rob houses along a street.
# Each house has some money
# Adjacent houses cannot be robbed (alarm!)
# You must maximize the total money robbed
# 👉 Return the maximum amount you can rob.
# 🧠 Key Insight (Read Slowly)

# At every house, you must make a choice:
# Rob it ❌ rob previous
# Skip it ✅ maybe rob previous
# This is your first “conflicting choice” DP.

# 1️⃣ Define the DP State (CRITICAL)
# dp[i] = maximum money you can rob from houses 0..i

# 2️⃣ Transition (Why this works)
# At house i:

# Option 1️⃣: Skip house i
# You get:
# dp[i-1]

# Option 2️⃣: Rob house i
# You must skip i-1, so you get:
# dp[i-2] + nums[i]

# ✅ Final recurrence:
# dp[i] = max(dp[i-1], dp[i-2] + nums[i])

# 3️⃣ Base Cases
# dp[0] = nums[0]
# dp[1] = max(nums[0], nums[1])

# 🧩 Example
# nums = [2,7,9,3,1]

# DP evolution:
# dp[0] = 2
# dp[1] = 7
# dp[2] = max(7, 2+9) = 11
# dp[3] = max(11, 7+3) = 11
# dp[4] = max(11, 11+1) = 12


# Answer = 12
# ✍️ Your Task
# Implement DP array solution
# Then try space-optimized
# Test on:
# [1,2,3,1]     → 4
# [2,7,9,3,1]   → 12
# [5]           → 5

# ⚠️ Common Mistakes
# ❌ Using greedy
# ❌ Forgetting i-2 when robbing
# ❌ Incorrect base cases

# 🧠 Problem 4 Pattern You’re Learning
# Decision DP with conflicting choices
# This pattern appears in:
# Scheduling
# Resource allocation
# Stock problems
# Interval DP later


def house_robber(houses):
    n = len(houses)
    if n == 0:
        return 0
    if n == 1:
        return houses[0]
      
    dp = [0] * n
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])
  
    for i in range(2, n):
        dp[i] = max(dp[i-2] + houses[i], dp[i-1])
    return dp[-1]
