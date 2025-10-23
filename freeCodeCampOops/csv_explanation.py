# Demonstration of csv.DictReader behavior

import csv
from io import StringIO

# Simulate a CSV file content
csv_content = """name,price,quantity
Phone,100,4
Laptop,1500,3
Tablet,300,2"""

# Create a file-like object from the string
csv_file = StringIO(csv_content)

print("=== Step by step breakdown ===")

# Step 1: Create DictReader
reader = csv.DictReader(csv_file)
print(f"1. reader type: {type(reader)}")
print(f"   reader object: {reader}")

# Step 2: Convert to list
csv_file.seek(0)  # Reset file pointer
reader = csv.DictReader(csv_file)
items = list(reader)

print(f"\n2. items type: {type(items)}")
print(f"   items length: {len(items)}")

print(f"\n3. What's inside the list:")
for i, item in enumerate(items):
    print(f"   items[{i}] type: {type(item)}")
    print(f"   items[{i}] content: {item}")

print(f"\n4. Accessing individual elements:")
for i, item in enumerate(items):
    print(f"   Row {i+1}:")
    print(f"     item.get('name'): {item.get('name')}")
    print(f"     item.get('price'): {item.get('price')}")
    print(f"     item.get('quantity'): {item.get('quantity')}")

print(f"\n5. This is why your loop works:")
print("   for item in items:")
print("       # item is a dictionary on each iteration")
print("       # so item.get('name') works!")