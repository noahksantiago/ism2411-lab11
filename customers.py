
print("--- Exercise 1: One Customer ---")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


print("--- Exercise 2: Update and Add ---")

customer["phone"] = "555-123-4567"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)


print("--- Exercise 3: Safe Lookup ---")
email = customer.get("email", "no email on file")
print(email)

try:
    print(customer["email"])
except KeyError as error:
    print("KeyError caught:", error)

print("--- Exercise 4: Iterate ---")
for key, value in customer.items():
    print(f"{key}: {value}")

for key in customer:
    print(key)


print("--- Exercise 5: Lookup Table ---")
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}
tier = customer["tier"]
discount = tier_discounts.get(tier, 0)
purchase = 200
final_price = purchase * (1 - discount)
print(f"Tier: {tier}")
print(f"Discount: {discount * 100:.0f}%")
print(f"Final Price: ${final_price:.2f}")


print("--- Exercise 6: List of Dictionaries ---")

customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "gold"},
    {"name": "Charlie", "tier": "silver"}
]
for person in customers:
    name = person["name"]
    tier = person["tier"]
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount_rate

    print(f"{name}: {tier}, Discount: ${discount_amount:.2f}")
