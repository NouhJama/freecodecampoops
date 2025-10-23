from item import Item

class Phone(Item):
    def __init__(self, name, price, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(name, price, quantity)

        # Validations for Phone class
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero!"

        # Attributes specific to Phone
        self.broken_phones = broken_phones

        # object representation
    def __repr__(self):
        # Object represention of this specific object
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.broken_phones})"