from item import Item
from phone import Phone  # Import the Phone  class
    
# Item.instantiate_from_csv()  # Create Item instances from CSV
# print(Item.all)  # Show all Item instances

item = Item("TestItem", 50, 10)
item._name = 'OtherName'
print(item.name)





