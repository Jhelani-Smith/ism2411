# Module 10 - Inventory List Manager
# Reflection 1:
# That for calling upon an item an a list '0' is the first item
#
# Reflection 2:
# In my calculus class I've had to sort and identify different numeralical patterns
# based on an equation and python's lists would have helped with that


# Exercise 1: Build the list
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2: Index practice
print(inventory[0])
print(inventory[-1])
middle_index = len(inventory) // 2
print(inventory[middle_index])

# Exercise 3: Slicing
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4: Modify
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# Exercise 5: Tuple comparison
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples are useful for coordinates because they cannot be changed.")

print(coords)

# Exercise 6: Average of a list of sales
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))

# Exercise 7: Accumulator pattern
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    discounted.append(round(price * 0.90, 2))

print(prices)
print(discounted)

# Exercise 8: Filter above threshold
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print(high_sales)
print("Count:", len(high_sales))
print("Avg:", round(sum(high_sales) / len(high_sales), 2))
