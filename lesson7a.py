# Functions Return Statements
# They used to return the results of a finction after execution, therefore the returned
# values can stored inside variable, to be used on another program

def multiply(a, b, c):
    print(a * b * c)



resuilt = multiply(10, 10, 10)
print(resuilt)

def sum(A, B, C):
    return A+B+C

def product(D):
    return D*2



answer = product(sum(20, 20, 20))
print(answer)
