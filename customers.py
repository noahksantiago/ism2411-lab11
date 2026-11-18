
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


print("--- Exercise 7: Nested Catalog ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}
for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} ({details['stock']} remaining)")


print("--- Exercise 8: Sales by Region ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]
region_totals = {}
for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    region_totals[region] = region_totals.get(region, 0) + amount
for region in sorted(region_totals):
    print(f"{region}: ${region_totals[region]}")

#1. i'd use get() when I'm workign with data that might have missing fields because
#it allows me to provide a default value instaed of crashing. I would use a bracket
#notation when I know a key should exist, since an error would help me find a problem
#in my data
#2. Buildign a summary dictionary reminds me of using a table in google sheets to 
#group data and calculate totals for different categories. Python can be useful for
#large datasets because it allows me to automate the rpocess and repeat it without
#manually updating a spreadsheet. 