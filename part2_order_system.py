menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}


# ---------------- TASK 1 ----------------


print("\n========== MENU ==========\n")

categories = set(item["category"] for item in menu.values())

for category in categories:
    print(f"===== {category} =====")
    for name, details in menu.items():
        if details["category"] == category:
            status = "Available" if details["available"] else "Unavailable"
            print(f"{name:15} ₹{details['price']:.2f}   [{status}]")
    print()

# Total items
total_items = len(menu)

# Available items
available_items = sum(1 for item in menu.values() if item["available"])

# Most expensive item
most_expensive = max(menu.items(), key=lambda x: x[1]["price"])

# Items under 150
cheap_items = [(name, data["price"]) for name, data in menu.items() if data["price"] < 150]

print("Total items:", total_items)
print("Available items:", available_items)
print("Most expensive item:", most_expensive[0], "₹", most_expensive[1]["price"])

print("\nItems under ₹150:")
for item in cheap_items:
    print(item[0], "₹", item[1])


# ---------------- TASK 2 ----------------

cart = []

def add_item(item_name, quantity):
    if item_name not in menu:
        print(f"{item_name} not in menu")
        return

    if not menu[item_name]["available"]:
        print(f"{item_name} is unavailable")
        return

    for item in cart:
        if item["item"] == item_name:
            item["quantity"] += quantity
            print(f"Updated {item_name} quantity to {item['quantity']}")
            return

    cart.append({
        "item": item_name,
        "quantity": quantity,
        "price": menu[item_name]["price"]
    })
    print(f"Added {item_name}")

def remove_item(item_name):
    for item in cart:
        if item["item"] == item_name:
            cart.remove(item)
            print(f"Removed {item_name}")
            return
    print(f"{item_name} not in cart")

def print_cart():
    print("\nCurrent Cart:")
    for item in cart:
        print(item)
    print()

# Simulation
add_item("Paneer Tikka", 2)
print_cart()

add_item("Gulab Jamun", 1)
print_cart()

add_item("Paneer Tikka", 1)
print_cart()

add_item("Mystery Burger", 1)
add_item("Chicken Wings", 1)

remove_item("Gulab Jamun")
print_cart()

# Order Summary
print("\n========== Order Summary ==========")

subtotal = 0

for item in cart:
    total = item["quantity"] * item["price"]
    subtotal += total
    print(f"{item['item']:15} x{item['quantity']}   ₹{total:.2f}")

gst = subtotal * 0.05
total_payable = subtotal + gst

print("------------------------------------")
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"GST (5%): ₹{gst:.2f}")
print(f"Total Payable: ₹{total_payable:.2f}")
print("====================================")


# ---------------- TASK 3 ----------------

import copy

inventory_backup = copy.deepcopy(inventory)

# Modify original
inventory["Paneer Tikka"]["stock"] = 5

print("\nModified Inventory:", inventory["Paneer Tikka"])
print("Backup Inventory:", inventory_backup["Paneer Tikka"])

# Restore
inventory = copy.deepcopy(inventory_backup)

# Deduct cart items
for item in cart:
    name = item["item"]
    qty = item["quantity"]

    if inventory[name]["stock"] >= qty:
        inventory[name]["stock"] -= qty
    else:
        print(f"Warning: Only {inventory[name]['stock']} {name} available")
        inventory[name]["stock"] = 0

# Reorder alert
print("\nReorder Alerts:")
for name, data in inventory.items():
    if data["stock"] <= data["reorder_level"]:
        print(f"⚠ Reorder Alert: {name} — Only {data['stock']} left")

print("\nFinal Inventory:", inventory)
print("\nBackup Inventory:", inventory_backup)

# ---------------- TASK 4 ----------------

def revenue_per_day(log):
    revenues = {}
    for date, orders in log.items():
        total = sum(order["total"] for order in orders)
        revenues[date] = total
        print(f"{date} → ₹{total}")
    return revenues

print("\nRevenue per day:")
revenues = revenue_per_day(sales_log)

# Best day
best_day = max(revenues, key=revenues.get)
print("Best selling day:", best_day)

# Most ordered item
item_count = {}

for orders in sales_log.values():
    for order in orders:
        for item in order["items"]:
            item_count[item] = item_count.get(item, 0) + 1

most_ordered = max(item_count, key=item_count.get)
print("Most ordered item:", most_ordered)

# Add new day
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

print("\nUpdated Revenue:")
revenues = revenue_per_day(sales_log)

best_day = max(revenues, key=revenues.get)
print("New Best Day:", best_day)

# Enumerate all orders
print("\nAll Orders:\n")

count = 1
for date, orders in sales_log.items():
    for order in orders:
        items = ", ".join(order["items"])
        print(f"{count}. [{date}] Order #{order['order_id']} — ₹{order['total']} — Items: {items}")
        count += 1

