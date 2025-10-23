# Dictionary .get() method demonstration

# Sample dictionary (like what csv.DictReader creates)
item_dict = {'name': 'Phone', 'price': '100', 'quantity': '4'}

print("=== Using .get() method ===")
print(f"Name: {item_dict.get('name')}")           # 'Phone'
print(f"Price: {item_dict.get('price')}")         # '100'
print(f"Quantity: {item_dict.get('quantity')}")   # '4'

print("\n=== Safe access with .get() ===")
print(f"Color: {item_dict.get('color')}")         # None (key doesn't exist)
print(f"Color with default: {item_dict.get('color', 'Unknown')}")  # 'Unknown'

print("\n=== Comparison: .get() vs direct access ===")
# Using .get() - safe
missing_value = item_dict.get('missing_key')
print(f"Missing key with .get(): {missing_value}")  # None

# Using direct access - would raise KeyError
try:
    missing_value = item_dict['missing_key']
except KeyError as e:
    print(f"Direct access error: {e}")

print("\n=== Real CSV scenario ===")
# Simulate what happens in your instantiate_from_csv method
csv_row = {'name': 'Tablet', 'price': '300', 'quantity': '2'}

# Extract values safely
name = csv_row.get('name')
price = float(csv_row.get('price'))  # Convert string to float
quantity = int(csv_row.get('quantity'))  # Convert string to int

print(f"Extracted - Name: {name}, Price: {price}, Quantity: {quantity}")