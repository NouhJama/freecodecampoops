class Duck:
    def quack(self):
        return "Duck Quacks!"
    
class Person:
    def quack(self):
        return "Person Imitates a Duck!"
    
#Polymorphism in action
def make_it_quack(duck_like):
    return duck_like.quack()

# Example usage
duck = Duck()
person = Person()
print(make_it_quack(duck))   # Output: Duck Quacks!
print(make_it_quack(person))  # Output: Person Imitates a Duck!