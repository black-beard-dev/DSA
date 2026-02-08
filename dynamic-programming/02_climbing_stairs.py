# 2.Climbing Stairs

# You are climbing a staircase with n steps.
# Each time, you can climb 1 step or 2 steps.
# 👉 How many distinct ways are there to reach the top?
# 🧠 Think Before Coding (Very Important)
# Step 1️⃣ — Define the DP state
# dp[i] = number of ways to reach step i
# Step 2️⃣ — Transition
# To reach step i:
# You could come from i - 1
# Or from i - 2
# This is kind of fibonacci but disguised
# So dp[i] = dp[i-1] + dp[i-2]

# Step 3️⃣ — Base cases
# dp[0] = 1   # one way: do nothing
# dp[1] = 1   # one way: 1 step
# ✍️ Your Task
# Implement DP with an array
# Test for:
# n = 0
# n = 1
# n = 2
# n = 5
# Expected Outputs
# n = 2 → 2
# n = 3 → 3
# n = 5 → 8

def climbing_stairs(n):
    if n <= 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# Explaination 
# You will have lots of questions why it works? Why dp[i] =  dp[i-1] + dp[i-2] etc etc
# Lets go step by step
# 🪜 What does climbing_stairs(n) mean?
# Number of distinct ways to reach step n
# That’s it. Nothing else.

# 🧠 Key Observation (Most Important Insight)

# To reach step n, what are the last possible moves?
# Only TWO possibilities:
# You came from step n-1 (1-step jump)
# You came from step n-2 (2-step jump)
# There are no other ways to land exactly on step n.

# 🔁 Breaking It Down
# Case 1️⃣: Last move was 1 step

# You were at step n-1.
# Number of ways to reach n this way =
# 👉 number of ways to reach n-1

# Which is:
# climbing_stairs(n-1)

# Case 2️⃣: Last move was 2 steps
# You were at step n-2.
# Number of ways to reach n this way =
# 👉 number of ways to reach n-2

# Which is:
# climbing_stairs(n-2)

# ➕ Why Do We Add Them?
# Because:
# All ways to reach n-1 are distinct from
# All ways to reach n-2
# And every valid path to n ends in exactly one of these two cases.
# So total ways:
# ways(n) = ways(n-1) + ways(n-2)

# That’s it. No trick. No formula.

# 🧩 Concrete Example: n = 4

# Let’s list actual paths:
# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2


# Total = 5 ways
# Now group them by the last move:

# Ending with 1 step (from 3):
# 1+1+1 | +1
# 1+2   | +1
# 2+1   | +1
# → climbing_stairs(3) ways

# Ending with 2 steps (from 2):
# 1+1 | +2
# 2   | +2
# → climbing_stairs(2) ways

# So:
# climbing_stairs(4) = climbing_stairs(3) + climbing_stairs(2)
#                    = 3 + 2
#                    = 5

# 🧠 DP Rule (Memorize This Forever)
# DP recurrence is based on the last decision, not the first.
# Ask:
# “What was the last move I made?”
# Example:

# climbing_stairs(5)
#  ├─ climbing_stairs(4)
#  │   ├─ climbing_stairs(3)
#  │   │   ├─ climbing_stairs(2)
#  │   │   └─ climbing_stairs(1)
#  │   └─ climbing_stairs(2)
#  └─ climbing_stairs(3)
# See the repetition? 👀



