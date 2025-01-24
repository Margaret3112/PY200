import doctest


class Table:
    def __init__(self, material: str, width: int):
        """
        Создание и подготовка к работе объекта "Стол"

        :param material: Материал
        :param width: Ширина

        Примеры:
        >>> table1 = Table(4, 30)
        Traceback (most recent call last):
        ...
        TypeError: Напишите материал буквами
        >>> table2 = Table('дерево', 25)
        Traceback (most recent call last):
        ...
        ValueError: Принимаем заказы на ширину стола не меньше 30
        >>> table3 = Table('металл', 'сорок')
        Traceback (most recent call last):
        ...
        TypeError: Напишите число

        """
        self.material = None
        self.check_material(material)
        self.width = None
        self.check_width(width)

    def check_material(self, material:str) ->None:
        if not isinstance(material, str):
            raise TypeError("Напишите материал буквами")
        self.material=material

    def check_width(self, width:int) -> None:
        if not isinstance(width,int):
            raise TypeError("Напишите число")
        if width <= 30:
            raise ValueError("Принимаем заказы на ширину стола не меньше 30")

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()