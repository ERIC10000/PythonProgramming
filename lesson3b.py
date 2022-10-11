# Tuples Data Type

# Unchangeable, Ordered, Allow duplicates
# Brackets ()

courses = ("Android", "Data Science", "Python")
language = ("Python",)
# type()

print(type(courses))
print(type(language))

# Accesing Elements -> Ordered index, starts from zero, []

print(courses[1])
print(courses)

x = list(courses)
print(x)

x.append("IoT")

courses = tuple(x)
print(courses)

# Create a tuples of 5 schools
# add 3 more schools to the tuple
