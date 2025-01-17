# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Table:
    def __init__(self, material: str, width: int):
        """
        Создание и подготовка к работе объекта "Стол"

        :param material: Материал
        :param width: Ширина

        Примеры:

        """
        self.material = None
        self.check_material(material)
        self.width = None
        self.check_width(width)

    def check_material(self,material):
        if not isinstance(material, str):
            raise TypeError("Напишите материал буквами")
        self.material=material

    def check_width(self,width):
        if not isinstance(width,int):
            raise TypeError("Напишите число")
        if width <= 30:
            raise ValueError("Принимаем заказы на ширину стола не меньше 30")

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
