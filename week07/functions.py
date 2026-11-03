##################################################################
#Disclosure comment
#I used AI to help me identify my coding errors and help me understand the instructions I did not get. 
# I did not use it as a cruth but I would like to use it less in the future
##################################################################
#Self-Assessment Questions 

1. #In Exercise 5 (Debug First, Then Ask), what was the first bug you spotted? The missing semicolon.
#Did you find it from the traceback, from a print() statement, from explaining the code out loud to the duck, or only after 
#asking AI? explaing the code line by line to my "duck" hellped me discover it.
# What does that tell you about your current debugging instincts? They need work.


2. #Without looking at your code, explain in plain English what apply_discount(price, tier) does, what its inputs are, 
#and what it returns. Could a colleague use it without reading the body? price is the cost of something, tier is the level
#of modifier you apply to the price based on certain factors. Apply discounts factors the final price with discounts
#factored in. Yes.


3. #If you used AI on any part of today's lab, write the disclosure comment you would add to the top of your file. 
#Then reflect: did the AI use build your understanding, or did it shortcut it?


##################################################################



#exercise 1
def calculate_tax(price, rate): 
    return price * rate
tax1 = calculate_tax(100, 0.07) 
tax2 = calculate_tax(250, 0.08)
print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")



#exercise 2
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else: 
        return price
price = 200
for tier in ["gold", "silver", "bronze", "none"]:
    discounted_price = apply_discount(price, tier)
    print(f"{tier}: ${discounted_price:.2f}")


#exercise 3
def final_price(price, tier, tax_rate):    
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax
discounted = apply_discount(200, "gold")
print(f"After gold discount: $ {discounted:.2f}") 
after_tax = discounted + calculate_tax(discounted, 0.07)
print(f"After tax: ${after_tax:.2f}")
print(f'final_price(200, "gold", 0.07) = $ {final_price(200, "gold", 0.07):.2f}')


#exercise 4
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


#exercise 5
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total = sale
print(f"Total: ${total}")



count = 0
#adding a colon at th end of sales with link it to the next line of code, eliminating the error
for sale in sales:
    count += 1
print(f"Count: {count}")



i = 0
while i <= len(sales):
    print(sales[4])
#print needed an actual value in he list
    i += 1


print("hello world!")
#exercise 6
x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # what prints here? x or 100
print(double_it()) # what prints here? two times 999 or 1998
print(x)           # has x changed? no the value is the same as there have been no alternations

