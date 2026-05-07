# ==========================================
# DAY 2: WHILE LOOPS & CONTROL FLOW
# Goal: Master iteration for system automation
# ==========================================

# --- Challenge 1: Count and Sum of Digits ---
# DevOps Use Case: Parsing log IDs or processing numeric telemetry data.
n = 12345
count = 0
sum_digits = 0
while n > 0:
    digit = n % 10
    sum_digits += digit
    n = n // 10
    count += 1
print(f"Total Digits: {count}, Sum: {sum_digits}")


# --- Challenge 2: Reverse a Number & Palindrome ---
# logic check: Reversing strings/numbers is common in data validation.
n = 12321
original = n
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original == reverse:
    print(f"{original} is a Palindrome")
else:
    print("Not a Palindrome")


# --- Challenge 3: Find Max and Min Number ---
# DevOps Use Case: Finding peak CPU usage or lowest latency in a list of metrics.
# (Simulating a stream of inputs)
numbers = [45, 12, 89, 3, 56]
count = 0
max_num = numbers[0]
min_num = numbers[0]

while count < len(numbers):
    if numbers[count] > max_num:
        max_num = numbers[count]
    if numbers[count] < min_num:
        min_num = numbers[count]
    count += 1
print(f"Max: {max_num}, Min: {min_num}")


# --- Challenge 4: Infinite Loop, Break, and Continue ---
# DevOps Use Case: Creating a "Waiting" script (e.g., waiting for a server to come online).
attempts = 0
while True:
    attempts += 1
    if attempts == 3:
        print("Skipping attempt 3 (Simulating a busy signal)")
        continue
    if attempts > 5:
        print("Server check timed out. Breaking loop.")
        break
    print(f"Checking server status... Attempt {attempts}")


# --- Challenge 5: The 'else' Suite with While ---
# logic check: Running a cleanup script ONLY if the loop finishes without breaking.
count = 1
while count <= 3:
    print(f"Backup in progress... Part {count}")
    count += 1
else:
    print("Backup completed successfully (Loop finished naturally).")