# ООП, ФП, ЛП
# SOLID, DDD, DRY, TDD, FSD(frontend), MVC, MVVM, FLUX
from __future__ import annotations  #


class Shape:
    ID = 1

    def area(self):
        """
        Площадь
        """
        return 0

    def perimeter(self):
        return 0

    def __str__(self) -> str:
        return self.__class__.__name__

    def render(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        new_width = self.width + other.width
        new_height = self.height + other.height
        return Rectangle(new_width, new_height)


def main():
    shapes: list[Shape] = [Circle(2), Rectangle(2, 2)]

    str(Circle(2).render())
    str(Circle.ID)

    for shape in shapes:
        print(shape)


if __name__ == '__main__':
    main()
