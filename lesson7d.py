from assignment5 import greet

hello = greet("Erick")
print(hello)


# Object Oriented Programming - Python
# It is a paradym(style) of programming, where everything is treated as an object
# a class -> A blueprint of an object
# An object -> Instance of a class

class Iphone():
    brand = "Apple"
    model = "Iphone X"
    color = "Gold"
    camera_MP = "12 MP"
    hdd = "128 GB"
    platform = "iOS 12.3"


iphone1 = Iphone()

print(iphone1.color)
print(iphone1.camera_MP)

iphone2 = Iphone()

schools = ["Nairobi SCH", "Jamuhuri High"]
print(type(schools))

number1 = int(10)

# constructors
# methods
# inheritance
