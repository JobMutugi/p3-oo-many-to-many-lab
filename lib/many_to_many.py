class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    # Returns all contracts for this author
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    # Returns all books this author has contracts for
    def books(self):
        return [contract.book for contract in self.contracts()]

    # Creates a contract for this author and given book
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    # Calculates the total royalties for this author
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        self._title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title

    # Returns all contracts for this book
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    # Returns all authors who signed a contract for this book
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author")
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of Book")
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("Royalties must be an integer")

        self._author = author
        self._book = book
        self._date = date
        self._royalties = royalties

        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @property
    def book(self):
        return self._book

    @property
    def date(self):
        return self._date

    @property
    def royalties(self):
        return self._royalties

    # Returns all contracts that match a given date, sorted by date
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in sorted(cls.all, key=lambda c: c.date) if contract.date == date]
