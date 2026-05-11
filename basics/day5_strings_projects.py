# ==========================================
# DAY 5: STRING MANIPULATION & MINI-PROJECTS
# Goal: Parsing and formatting infrastructure data
# ==========================================

# --- 1. Indexing & Slicing ---
# DevOps Use Case: Extracting specific IDs from a long resource ARN.
resource_id = "arn:aws:ec2:us-east-1:123456789012:instance/i-0abcd1234efgh5678"

# Slicing the instance ID from the end
instance_id = resource_id[-19:] 
print(f"Extracted Instance ID: {instance_id}")

# Slicing the region
region = resource_id[12:21]
print(f"Region: {region}")


# --- 2. String Operations (Formatting) ---
# Goal: Standardizing log messages.
user = "admin"
action = "deleted_bucket"
message = f"User [{user.upper()}] performed action: {action.replace('_', ' ').title()}"
print(f"Log Entry: {message}")


# --- 3. Project: Restaurant Menu ---
# Logic: Using alignment and string multiplication for clean CLI output.
print("\n" + "="*20)
print("  RESTAURANT MENU  ")
print("="*20)
item1, price1 = "Burger", 120
item2, price2 = "Coffee", 50
print(f"{item1.ljust(15)}: Rs.{str(price1).rjust(4)}")
print(f"{item2.ljust(15)}: Rs.{str(price2).rjust(4)}")
print("="*20)


# --- 4. Project: Card Payment Receipt ---
# Logic: Masking sensitive data (like a credit card number or API key).
card_no = "4582123456789012"
masked_card = "*" * 12 + card_no[-4:]
print(f"\nPayment Receipt")
print(f"Card Number: {masked_card}")
print("Status: SUCCESS")