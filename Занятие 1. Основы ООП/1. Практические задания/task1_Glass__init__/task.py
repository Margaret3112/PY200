from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Класс 'Стакан'
        :param capacity_volume: Объем стакана (вместимость)
        :param occupied_volume: Занятый объём (сколько налили в стакан)
        """

        self.capacity_volume = None
        self.occupied_volume = None
        self.check(capacity_volume, occupied_volume )

    def check(self, capacity, occupied):
        if not isinstance(capacity, (int, float)):
            raise TypeError('Неверный тип')
        if not isinstance(occupied, (int, float)):
            raise TypeError('Неверный тип')
        if capacity<=0 or occupied>capacity or occupied<0:
            raise ValueError('Ошибка в числе')
        self.capacity_volume = capacity
        self.occupied_volume = occupied
        # TODO создайте атрибут capacity_volume и occupied_volume Обязательно проверяйте типы (TypeError) и значения передаваемых аргументов (ValueError)

if __name__ == "__main__":
    # TODO инициализировать два объекта от класса Стакан (Glass)

    try:
       a = Glass('d', 6)
       b = Glass(-1, 100)
        # TODO инициализировать не корректные объекты
    except Exception as err:
        print(f"Была вызвана ошибка {err!r}")
    else:
        print("Данный код без ошибок")


