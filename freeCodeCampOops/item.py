import csv

class Item:
    all = []
    pay_rate = 0.8 # The pay rate after 20% discount
    def __init__(self, name, price, quantity=0):
        # Validations
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        # Attributes
        self._name = name
        self.quantity = quantity
        self.price = price

        # Actions to execute
        Item.all.append(self) # Append the instance to the class attribute list

    @property
    def name(self):
        return self._name

    def calculate_total_price(self):
        return self.quantity * self.price
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)  # Iterator of dictionaries
            items = list(reader)        # Convert iterator to LIST OF DICTIONARIES
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"