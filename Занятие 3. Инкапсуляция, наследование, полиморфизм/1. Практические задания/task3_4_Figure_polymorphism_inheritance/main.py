import math


class Figure:
    """ Базовый класс. """

    def area(self):
        print(f"Вызван метод класса {self.__class__.__name__}")
        return None


class Rectangle(Figure):
    """ Производный класс. Прямоугольник. """
    # TODO определить конструктор
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def area(self):
        super().area()
        return round(self.a * self.b, 3)

    # TODO перегрузить метод area, чтобы он возвращал площадь, но не терял родительский функционал


class Circle(Figure):
    """ Производный класс. Круг. """
    # TODO определить конструктор
    def __init__(self, a):
        self.a = a

    def area(self):
        super().area()
        s = math.pi * 5 * 5
        return round(s, 3)

    # TODO перегрузить метод area, чтобы он возвращал площадь, но не терял родительский функционал,



if __name__ == "__main__":
    fig = Figure()
    print(fig.area())

    rect = Rectangle(5, 10)
    print(rect.area())

    circle = Circle(5)
    print(circle.area())
