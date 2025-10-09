class shape:
    def calculate_area(self):
        return f"shape area"

# Single Inheritance demonstration
class rectangle(shape):
    def calculate_area(self, length, breadth):
        return length * breadth
    
# Example usage
rect = rectangle()
print(f"Rectangle Area: {rect.calculate_area(5, 10)}")  # Output: Rectangle Area: 50