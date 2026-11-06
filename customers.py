# EXERCISE 1 — Basic Customer Dictionary
customer = {
    "customer_id": 1001,
    "name": "Alice Smith",
    "email": "alice@example.com",
    "tier": "Gold"
}

print("--- EXERCISE 1 ---")
print(customer)

# EXERCISE 2 — Accessing and Modifying Values
print("
--- EXERCISE 2 ---")
print("Name:", customer["name"])
print("Tier before update:", customer["tier"])

customer["tier"] = "Platinum"
print("Tier after update:", customer["tier"])

customer["phone"] = "555-0199"
print("Updated Customer Dictionary:", customer)

# EXERCISE 3 — Using .get() Method
print("
--- EXERCISE 3 ---")
print("Email:", customer.get("email"))
discount = customer.get("discount_rate", 0.10)
print("Discount Rate:", discount)

# EXERCISE 4 — Iterating Through Keys and Values
print("
--- EXERCISE 4 ---")
print("Customer Details:")
for key, value in customer.items():
    print(f"- {key}: {value}")

# EXERCISE 5 — List of Customer Dictionaries
print("
--- EXERCISE 5 ---")
customers = [
    {"customer_id": 1001, "name": "Alice Smith", "tier": "Platinum"},
    {"customer_id": 1002, "name": "Bob Jones", "tier": "Silver"},
    {"customer_id": 1003, "name": "Charlie Brown", "tier": "Gold"}
]

for c in customers:
    print(f"ID: {c[\"customer_id\"]}, Name: {c[\"name\"]}, Tier: {c[\"tier\"]}")

# EXERCISE 6 — Filtering a List of Dictionaries
print("
--- EXERCISE 6 ---")
print("Gold Tier Customers:")
for c in customers:
    if c["tier"] == "Gold" or c["tier"] == "Platinum":
        print(c["name"])

# EXERCISE 7 — Adding a Transaction History
print("
--- EXERCISE 7 ---")
customer_with_tx = {
    "customer_id": 1001,
    "name": "Alice Smith",
    "purchases": [150.50, 42.00, 89.99]
}

total_spent = sum(customer_with_tx["purchases"])
print(f"Total spent by {customer_with_tx[\"name\"]}: ${total_spent:.2f}")

# EXERCISE 8 — Advanced: Sales by region
print("
--- EXERCISE 8 ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
    {"region": "East", "amount": 450},
    {"region": "North", "amount": 50}
]

region_summary = {}

for tx in transactions:
    reg = tx["region"]
    amt = tx["amount"]
    region_summary[reg] = region_summary.get(reg, 0) + amt

print("Regional Sales Summary:")
for reg in sorted(region_summary.keys()):
    print(f"{reg}: {region_summary[reg]}")
