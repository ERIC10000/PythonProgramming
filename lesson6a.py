# Functions = This a Block of code that is performing a related task
# 2 categories of function
# 3. Enclosed inside brackets
# Inbuilt Function, print(), input(), type(), int().....
# User-Defined functions
# keyword def,
# function name
# brackets
# full colon
# Any item of a function is indented -

# add two number
# creating
def add():
    a = 10
    b = 20
    sum = a + b
    # print(sum)


# calling a function
# name, followed by the brackets
add()


# create and call a function that computes the area of a circle

def area_circle():
    PI = 3.142
    radius = 10
    area = PI * (radius ** 2)
    print(area)


# Parameters -> Values that are passed inside a function
def multiply(num1, num2):
    product = num1 * num2
    print(product)


# multiply()
#
# for count in range(10):
#     print(count)

def greet(name):
    print("Hey {}".format(name))


greet("Erick")


# Using function create a bmi calculator
def bmi_calculator(weight, height=1.5):
    bmi = weight / (height ** 2)
    print(bmi)
    return bmi


bmi_calculator(50, 1.7)


