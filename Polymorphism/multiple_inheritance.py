class Bird:
    def fly(self):
        return "Flying"
    
class Mammal:
    def walk(self):
        return "Walking"

# Multiple Inheritance demonstration
class Bat(Bird, Mammal): # Bat inherits from both Bird and Mammal
    def use_wings(self):
        return "Using wings to fly and walk"
    
# Example usage
bat = Bat()
print(bat.fly())      # Output: Flying
print(bat.walk())     # Output: Walking
print(bat.use_wings())# Output: Using wings to fly and walk
