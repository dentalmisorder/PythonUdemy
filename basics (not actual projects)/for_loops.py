prices = [3.55, 2.99, 3.99, 6.99, 9.99]

total_price = 0.0
for price in prices:
    total_price += price
    print(f"Adding item that costs {price}$")

print(f"Total: {total_price}")