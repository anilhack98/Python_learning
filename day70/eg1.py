class Rectangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width
    @classmethod
    def square(cls,size):
        return cls(size,size)
rectangle=Rectangle.square(10)
print(rectangle.height)
print(rectangle.width)
print(f"Area of rectangle is {rectangle.height * rectangle.width}")