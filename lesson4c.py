# if..elif...else

# Grading System logical operators
# 0 - 40 -> D
# 41 - 50 -> C
# 51- 69 -> B
# 70-100 -> A
# Above 100, less than 0 invalid mark

marks = int(input(" Enter Your Marks : "))

if marks > 0 and marks<=40:
    print("You scored D")
elif marks > 40 and marks<=50:
    print(" You Scored C")
elif marks > 50 and marks <= 69:
    print(" You Scored B")
elif marks >= 70 and marks <=100:
    print(" You Scored A")

else:
    print("Invalid mark!")
