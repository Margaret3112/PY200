# База данных книг для проверки
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_, name, pages):
        self.id = id
        self.name = name
        self. pages = pages
         # TODO дописать метод

    def __str__(self):
        return f' Книга "{self.__class__.__name__}"'
         # TODO дописать метод

    def __repr__(self):
        return f" Book(id_={self.id}, name='{self.name}', pages={self.pages})"
         # TODO дописать метод


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
