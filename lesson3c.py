# Python Dictionaries
# Hold a collection of keys with their value
# Changeable, Ordered, No duplicates allowed
# JSON file -> dictionary (APIs)
# JavaScript Object Notation
# Creared using braces {}

student = {
    "name": "Rodney",
    "age": 20,
    "course": "Software Development",
    "gender": "Male",
    "age": 34,
    "courses": ["Android", "Python", "Machine Learning"]
}

# Operations
# accessing elements

print(student)

print(student["name"])
print(student)

x = student.keys()
y = student.values()

z = student.items()
print(x)
print(y)
print(z)


student["height"] = 1.8
print(student)

student["course"] = "Cyber Security"
print(student)

student.pop("gender")
print(student)

# Sets
# Conditions (COMPARISON AND LOGICAL OPERATORS)
