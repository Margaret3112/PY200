class Date:
    def __init__(self, day: int, month: int, year: int):
        # TODO Инициализируйте переменные с проверкой соответствия типа, если не соответствует, то вызывайте ошибку TypeError
        self.day = day
        self.check_day(day)
        self.month = month
        self.check_month(month)
        self.year = year
        self.check_year(year)
    def __str__(self):
        return f"{self.day:0>2}/{self.month:0>2}/{self.year:4}"
        # TODO Реализуйте возвращение в формате DD/MM/YYYY

    def __repr__(self):
        return f"Date(day={self.day}, month={self.month}, year={self.year})"
         # TODO Реализуйте возвращение в формате Date(day=..., month=..., year=...)

    def check_day(self, d):
        if not isinstance(d,int):
            raise TypeError

    def check_month(self, m):
        if not isinstance(m, int):
            raise TypeError

    def check_year(self, y):
        if not isinstance(y, int):
            raise TypeError


if __name__ == "__main__":
    date1 = Date(1, 1, 2021)
    print(date1)  # 01/01/2021
    date2 = Date(11, 10, 1999)
    print(date2)  # 11/10/1999
    print(repr(date1), repr(date2))  # Date(day=1, month=1, year=2021) Date(day=11, month=10, year=1999)

    try:
        Date('1', 1, 2021)
    except TypeError:
        print('Верный вызов TypeError')  # Верный вызов TypeError
    else:
        print('Должен быть вызов TypeError')
