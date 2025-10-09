'''
Polymorphism through duck typing example in Python.
'''
class Dog:
    def make_sound(self):
        return "Dog Barks!"
class Cat:
    def make_sound(self):
        return "Cat Meows!"

class Bird:
    def make_sound(self):
        return "Bird Chirps!"
    
# Function that takes any animal and calls its make_sound method
def animal_sound(animal):
    return animal.make_sound()


#Create a list of objects from the classes above
animal_list =  [
    Dog(),
    Cat(),
    Bird()
]

def let_them_speak(animal_list): # Function to demonstrate duck typing
    for animal in animal_list: # Iterate through the list of animals
        print(animal_sound(animal)) # Call the function to make each animal sound

# Call the function to make the animals speak
let_them_speak(animal_list)