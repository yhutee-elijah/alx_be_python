import math

class Shape:
    """Represents a generic shape with an area method to be overridden.""" 

    def area(self):
        """This method should be overridden by subclasses."""
        raise NotImplementedError("Subclasses must override the area()method.")      

class Rectangle(Shape):
    """Represents a rectangle with a calculable area."""
    
    def __init__(self, length, width):
        """Initializes the rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width 
    
class Circle(Shape):
    """Represents a circle with a calculable area."""
    
    def __init__(self, radius):
        """Initializes the circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)
 
