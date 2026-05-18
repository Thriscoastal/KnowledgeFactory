# my first checkout program
print("--- Welcome to FreshMart Checkout ---") 
print("starting new transaction") # just printing to track it

name = "FreshMart"
id = 8402
tax = 0.07
vip = True
items = ["Apple", "Milk", "Bread"]
prices = {"Apple": 1.20, "Milk": 2.50}

# function for discounts
def calc_total(sub, vip):
    if vip == True and sub > 10.00:
        return sub * 0.85 
    elif vip == True:
        return sub * 0.90
    else:
        return sub

total = 0.0

# loop through the cart
for i in items:
    # have to check if it exists or python crashes
    if i in prices:
        p = prices[i]
    else:
        p = 0.0
        
    total = total + p
    print("Scanned: " + i + " -> $" + str(p))

# waiting for card swipe
tries = 0
while tries < 1:
    print("Waiting for customer card swipe...")
    tries = tries + 1

print("\n--- Error Handling Demo ---")

# my program kept crashing on bread so I added a try except block
try:
    bread_price = prices["Bread"] 
except:
    print("ERROR: barcode not found!")