# ==========================================
# DAY 3: FOR LOOPS & ITERATION
# Goal: Efficiently processing collections of data
# ==========================================

# --- Challenge 1: Factorial of a Number ---
# logic check: Factorials help understand accumulators, 
# which are used for calculating total uptime or resource usage.
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Factorial of {n} is: {factorial}")


# --- Challenge 2: Fibonacci Series ---
# logic check: This helps master state management between iterations.
terms = 10
a, b = 0, 1
print("Fibonacci Series:", end=" ")
for _ in range(terms):
    print(a, end=" ")
    a, b = b, a + b
print() # New line


# --- Challenge 3: Prime Number Check ---
# DevOps Use Case: Validating unique IDs or security tokens.
num = 17
is_prime = True
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
else:
    is_prime = False

print(f"Is {num} prime? {is_prime}")


# --- Challenge 4: Iterating over Collections ---
# DevOps Use Case: Running a health check across multiple regions.
regions = ["us-east-1", "us-west-2", "ap-south-1", "eu-central-1"]

for region in regions:
    print(f"Deploying infrastructure to: {region}")