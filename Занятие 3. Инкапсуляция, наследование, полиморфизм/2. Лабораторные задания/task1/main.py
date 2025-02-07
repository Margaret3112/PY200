class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__validation_name(name)
        self.__name = name
        self.__validation_author(author)
        self.__author = author

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    @staticmethod
    def __validation_name(name):
        if not isinstance(name, str):
            raise TypeError

    @staticmethod
    def __validation_author(author):
        if not isinstance(author, str):
            raise TypeError

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages
        self.pages_check(pages)

    @staticmethod
    def pages_check(pages):
        if not isinstance(pages, int):
            raise TypeError

    def __str__(self):
        super().__str__()

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration
        self.check_duration(duration)

    def __str__(self):
        super().__str__()

    @staticmethod
    def check_duration(duration):
        if not isinstance(duration, float):
            raise TypeError

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


