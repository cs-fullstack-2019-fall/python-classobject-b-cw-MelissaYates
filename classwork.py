# # python-classObject_b-cw
#
# Start with a main function and make each problem a function. Call those functions from your main function.
#
# ### Problem 1:
# Create a class Dog. Make sure it has the attributes name, breed, color, gender. Create a function that will print all attributes of the class.
# Create an object of Dog in your problem1 function and print all of it's attributes.
#
class Dog:
    def __init__(self, breed, color, gender):
        self.breed = breed
        self.color = color
        self.gender = gender
    def characteristics(self):
        print(f'{self.breed}, {self.color}, {self.gender}')

def problem1():
    dogType = Dog("Husky", "brown", "male")
    dogType.characteristics()
# ### Problem 2:
# ##### We will keep having this problem until EVERYONE gets it right without help
# Create a function that has a loop that quits with the equal sign. If the user doesn't enter the equal sign, ask them to input another string.
#
def problem2():
    userInput = input("Enter '=' to quit ")
    while userInput != '=':
        userInput = input("Enter another string. Enter '=' to quit ")
# ### Problem 3:
# Create a class Product that represents a product sold online. A product has a name, price, and quantity.
#
# The class should have several functions:
#
# a) One function that can change the name of the product.
#
# b) Another function that can change the name and price of the product.
#
# c) A last function that can change the name, price, and quantity of the product.
#
#     Create an object of Product and print all of it's attributes.
#
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def changeProdName(self, newProduct):
        self.name = newProduct

    def changePNameAndPrice(self, newProduct1, newPrice):
        self.name = newProduct1
        self.price = newPrice

    def changeProdAttributes(self, newProduct2, newPrice1, newQuantity):
        self.name = newProduct2
        self.price = newPrice1
        self.quantity = newQuantity


    def printAllOfAttributes(self):
        print(f'{self.name}, ${self.price}, {self.quantity}')

def problem3():
    prodOption = Product("Pants", "45.00", "2")
    prodOption.printAllOfAttributes()
    prodOption.changeProdName("Dress")
    prodOption.printAllOfAttributes()
    prodOption.changePNameAndPrice("Blouse", "20.00")
    prodOption.printAllOfAttributes()
    prodOption.changeProdAttributes("Jacket", "30.00", "3")
    prodOption.printAllOfAttributes()




def main():
    #problem1()
    #problem2()
    problem3()
main()