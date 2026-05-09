# Day 4: Mastering Iteration
# logic: For loops are the backbone of bulk infrastructure tasks.

# 1. Factorial logic (Accumulator Pattern)
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"Factorial of {n} is {fact}")

# 2. Fibonacci (State Management)
a, b = 0, 1
print("Fibonacci:", end=" ")
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b

# 3. DevOps Use Case: Iterating through a Server List
servers = ["web-01", "db-01", "cache-01"]
for server in servers:
    print(f"\nChecking health for {server}...")
    # Logic: if health == 'ok' print 'Healthy'