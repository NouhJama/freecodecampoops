class Item:
    all = []
    pay_rate = 0.8 # The pay rate after 20% discount
    def __init__(self, name, price, quantity=0):
        # Validations
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        # Attributes
        self.name = name
        self.quantity = quantity
        self.price = price

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.quantity * self.price
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item("Phone", 100, 4) # Create an instance of Item and set attributes
item2 = Item("Laptop", 1500, 3) # Create another instance of Item and set attributes
item3 = Item("Cable", 10, 5) # Create another instance of Item and set attributes
item4 = Item("Mouse", 50, 2) # Create another instance of Item and set attributes
item5 = Item("Keyboard", 75, 1) # Create another instance of Item

item1.pay_rate = 0.9 # Override the class attribute for this instance only
item1.apply_discount() # Apply discount using the instance's pay_rate
print(f"item1 price after discount: {item1.price}")

item2.pay_rate = 0.7 # Override the class attribute for this instance only
item2.apply_discount() # Apply discount using the class's pay_rate
print(f"item2 price after discount: {item2.price}")

for instance in Item.all:
    print(f"{instance.name}")

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

# print(Item.pay_rate) # Print the pay rate using the class name
# print(item1.pay_rate) # Print the pay rate using the instance name

# # Use this magic method to see all attributes of an instance or class for debugging or to see what is inside it.
# print(item1.__dict__) # Print the attributes of item1
# print(Item.__dict__) # Print the attributes of the Item class
