# initialize total price   
total_price = 0

print("Welcome to store checkout")
number_of_items = int(input("Enter number of items: "))


for i in range(number_of_items):
    price = float(input(f"Enter price of item {i + 1}: "))
    total_price += price  # Add each item's price to total

print(f"total price: {total_price:.2f}")

payment_amount = float(input(f"Enter payment amount: "))

change = payment_amount - total_price

if payment_amount > total_price:
     print(f"Payment accepted, here is your change: {change:.2f}")  # Format changed to two decimal places

elif payment_amount < total_price:
     print("Insufficient funds")

else:
     print("Payment successful")




