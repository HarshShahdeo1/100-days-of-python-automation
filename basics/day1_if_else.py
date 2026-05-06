# Day 1 Challenge: Budget Monitor
current_spend = 120  # Total spent on AWS this month
budget_limit = 100   # Your limit to avoid loan stress!

if current_spend > budget_limit:
    print("ALERT: Budget exceeded! Stopping non-essential instances.")
elif current_spend > (budget_limit * 0.8):
    print("Warning: You have used 80% of your budget.")
else:
    print("Budget is healthy. Keep building.")