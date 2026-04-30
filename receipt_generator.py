available_items = ["Mouse", "Keyboard", "Cable"]
shop_info = {"name": "Nepal Tech", "currency": "NPR"}

name = input("Enter Customer Name: ")
price = float(input("Enter Item Price: "))
quantity = int(input("Quantity: "))

total = price * quantity
if total > 1000:
    status = "Premium Customer"
else:
    status = "Standard Customer"

package_contents = " & ".join(available_items)

print(f"\n--- {shop_info['name']} ---")
print(f"Customer: {name} ({status})")
print(f"Items inside: {package_contents}")
print(f"Total Amount: {shop_info['currency']} {total}")
