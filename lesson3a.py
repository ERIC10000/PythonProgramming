# Data Types
# 1.String, Integer, Float , Booleans
# Arrays -> A collection of items together
# List, Tuple, Dictionary, Sets

# List Data Type
# It contains a list of changeable, ordered, allow duplicates items
# Enclosed inside Squared Brackets []


countries = ["Kenya", "Somalia", "uganda", "Tanzania"]
numbers = [10, 30, 30, 40, 50]
instances = [True, False, False, True]

conties = ["Nairobi", 47, "Mombasa", 1, True, 20.45]

# List Operations
# 1.Length -> len()
# Type -> type()

print(len(countries))
print(type(countries))

# Accessing Items on a list
# 1. Index -> Starts from Zero, []
# 2.range ->First item is included, the last item is excluded

print(numbers[0])
print(countries[1:3])

fruits = ["Grapes", "Beetroot", "Banana", "Oranges", "Pinneapple"]
# print out the third and the fourth element
# the last element

# Check existence of an element (in, not in)
if "Apple" not in fruits:
    print("Banana Exist")

# Adding, Replacing an element, add list to a list
# append() -> Adds a nwe element to the clist
fruits.append("Apple")
print(fruits)

# Replacing an element

fruits.insert(1, "Oranges")
print(fruits)

# extend() -> Adds list to a list

fruits.extend(countries)
print(fruits)

# Removing items from list
# index -> pop()
# element -> remove()

fruits.pop(7)
print(fruits)

fruits.remove("Pinneapple")
print(fruits)

# all the element -> clear()

fruits.clear()
print(fruits)

del fruits
# assignment2.py
# create a list of 6 students.
# 1. Add 2 new students
# Show the 4th to 7th student
# Replace the 3rd student

# check if a certain student is not existing, add the student.NB student should not be existing

students = ["james", "lucy", "Miriam", "Antony", "Patrick", "Andrew"]
newStudents = ["Joseph", "Kelvin"]

students.extend(newStudents)

print(students)

print(students[3:7])

# students.insert(2, "Nancy") -> adding a new element
students[2] = "Nancy"
print(students)

if "Nancy" not in students:
    students.append("Maxwell")
    print(students)
# print(students)
