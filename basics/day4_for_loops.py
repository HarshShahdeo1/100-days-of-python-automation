# ==========================================
# DAY 4: NESTED LOOPS & MATCH CASE
# Goal: Managing hierarchical data & clean branching
# ==========================================

# --- Challenge 1: Prime Numbers from 1-100 ---
# Logic: Using a loop inside a loop to filter data.
print("Prime Numbers 1-100:")
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print("\n" + "-"*30)


# --- Challenge 2: Drawing Patterns (Grid Logic) ---
# DevOps Use Case: Visualizing resource clusters or matrix-based monitoring.
print("Resource Grid Visualization:")
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print() # Moves to the next "row"
print("-"*30)


# --- Challenge 3: Match Case (Python 3.10+) ---
# DevOps Use Case: Handling different HTTP status codes or API responses.
status_code = 404

match status_code:
    case 200:
        print("Success: Server is healthy.")
    case 404:
        print("Error: Resource not found. Check the S3 bucket path.")
    case 500:
        print("Critical: Internal Server Error. Check the logs.")
    case _:
        print("Unknown Status: Triggering generic alert.")