from abc import ABC, abstractmethod
import math

class InvalidPointError(Exception):
    def __init__(self, message="Points must be valid instances of the Point class."):
        super().__init__(message)

class InvalidDimensionError(Exception):
    def __init__(self, message="Width and height must be greater than zero."):
        super().__init__(message)

class NotASquareError(Exception):
    def __init__(self, message="The given points do not form a valid square."):
        super().__init__(message)

class Shape(ABC):
    def __init__(self, name):
        self._name = name  

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    @abstractmethod
    def compute_area(self):
        pass

    @abstractmethod
    def compute_perimeter(self):
        pass

    @abstractmethod
    def compute_inner_angles(self):
        pass

    @abstractmethod
    def is_it_regular(self):
        pass

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
      
    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    def distance_to(self, other_point):
        return math.sqrt((self._x - other_point.get_x()) ** 2 + (self._y - other_point.get_y()) ** 2)

    def __repr__(self):
        return f"({self._x}, {self._y})"

class Line:
    def __init__(self, start_point, end_point):
        self.__start = start_point
        self.__end = end_point

    def length(self):
        return self.__start.distance_to(self.__end)

class Rectangle(Shape):
    def __init__(self, point1, point2):
        super().__init__("Rectangle")

        if not hasattr(point1, "get_x") or not hasattr(point1, "get_y"):
            raise InvalidPointError("point1 is not a valid point.")
        if not hasattr(point2, "get_x") or not hasattr(point2, "get_y"):
            raise InvalidPointError("point2 is not a valid point.")

        self.__point1 = point1
        self.__point2 = point2
        self.__width = abs(point2.get_x() - point1.get_x())
        self.__height = abs(point2.get_y() - point1.get_y())

        if self.__width == 0 or self.__height == 0:
            raise InvalidDimensionError("A rectangle cannot have zero width or height.")

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def set_width(self, w):
        if w <= 0:
            raise InvalidDimensionError("Width must be greater than zero.")
        self.__width = w

    def set_height(self, h):
        if h <= 0:
            raise InvalidDimensionError("Height must be greater than zero.")
        self.__height = h

    def compute_area(self):
        return self.__width * self.__height

    def compute_perimeter(self):
        return 2 * (self.__width + self.__height)

    def compute_inner_angles(self):
        return [90, 90, 90, 90]

    def is_it_regular(self):
        return self.__width == self.__height

class Square(Rectangle):
    def __init__(self, p1, p2):
        super().__init__(p1, p2)
        self._name = "Square"
        
        if self.get_width() != self.get_height():
            raise NotASquareError("Width and height must be equal to form a square.")

    def is_it_regular(self):
        return True

def main():
    p1 = Point(0, 0)
    p2 = Point(5, 5)

    rect = Rectangle(p1, p2)
    print("Rectangle area:", rect.compute_area())
    print("Rectangle perimeter:", rect.compute_perimeter())
    print("Is rectangle regular?", rect.is_it_regular())

    sq = Square(p1, p2)
    print("Square area:", sq.compute_area())
    print("Square perimeter:", sq.compute_perimeter())
    print("Is square regular?", sq.is_it_regular())

if __name__ == "__main__":
    main()
