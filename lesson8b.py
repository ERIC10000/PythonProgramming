# square

class Square:
    def __int__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        area = self.width * self.height
        print(area)

    # perimeter
    # (width+height) * 2
square1 = Square()
square1.width = 10
square1.height = 10

square1.area()

# create a class Triangle, with 3 properties and 2 methods
