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

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item("Phone", 100, 4) # Create an instance of Item and set attributes
item2 = Item("Laptop", 1500, 3) # Create another instance of Item and set attributes
item3 = Item("Cable", 10, 5) # Create another instance of Item and set attributes
item4 = Item("Mouse", 50, 2) # Create another instance of Item and set attributes
item5 = Item("Keyboard", 75, 1) # Create another instance of Item and set attributes

item1.pay_rate = 0.9 # Override the class attribute for this instance only
item1.apply_discount() # Apply discount using the instance's pay_rate
print(f"item1 price after discount: {item1.price}")
item2.pay_rate = 0.7 # Override the class attribute for this instance only
item2.apply_discount() # Apply discount using the class's pay_rate
print(f"item2 price after discount: {item2.price}")

print(Item.all)  # Show all instances