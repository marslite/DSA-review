class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self,x,y):
        self.x = x
        self.y = y


class Rectangle(Shape):
    def __init__(self,x,y,w,h):
        super().__init__(x,y)
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self,x,y,r):
        super().__init__(x,y)
        self.r = r
    def area(self):
        return 3.14*self.r*self.r
    


def print_area(shapes):
    for shape in shapes:
        print(shape.area())


rectangle = Rectangle(0,0,4,5);
circle = Circle(2,2,4);
shapes = [rectangle,circle];
rectangle.move(20,20)
print(rectangle.x, rectangle.y, rectangle.w, rectangle.h);