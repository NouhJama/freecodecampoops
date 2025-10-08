class Item:
    pay_rate = 0.8  # Class attribute
    
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

# Create instances
item1 = Item("Phone", 100, 4)
item2 = Item("Laptop", 1000, 2)

print("=== Before customization ===")
print(f"item1.pay_rate: {item1.pay_rate}")  # 0.8 (from class)
print(f"item2.pay_rate: {item2.pay_rate}")  # 0.8 (from class)
print(f"Item.pay_rate: {Item.pay_rate}")    # 0.8 (class attribute)

# Customize pay_rate for item1 only
item1.pay_rate = 0.9  # Now item1 has its own instance attribute

print("\n=== After customization ===")
print(f"item1.pay_rate: {item1.pay_rate}")  # 0.9 (instance attribute)
print(f"item2.pay_rate: {item2.pay_rate}")  # 0.8 (still from class)
print(f"Item.pay_rate: {Item.pay_rate}")    # 0.8 (unchanged)

# Apply discounts
print(f"\nitem1 price before discount: {item1.price}")
item1.apply_discount()
print(f"item1 price after discount: {item1.price}")  # Uses 0.9

print(f"\nitem2 price before discount: {item2.price}")
item2.apply_discount()
print(f"item2 price after discount: {item2.price}")  # Uses 0.8

# Show the difference in __dict__
print(f"\nitem1.__dict__: {item1.__dict__}")  # Contains pay_rate
print(f"item2.__dict__: {item2.__dict__}")  # No pay_rate