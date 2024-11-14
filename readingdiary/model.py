from datetime import datetime


class Note:
    def __init__(self, text: str, page: int, date: datetime):
        self.text: str = text
        self.page: int = page
        self.date: datetime = date

    def __str__(self) -> str:
        return f"{self.date} - page {self.page}: {self.text}"


class Book:
    EXCELLENT: int = 3
    GOOD: int = 2
    BAD: int = 1
    UNRATED: int = -1

    def __init__(self, isbn: str, title: str, author: str, pages: int):
        self.isbn: str = isbn
        self.title: str = title
        self.author: str = author
        self.pages: int = pages
        self.rating: int = Book.UNRATED
        self.notes: list[Note] = []

    def add_note(self, text: str, page: int, date: datetime) -> bool:
        if page > self.pages:
            return False
        new = Note(text, page, date)
        self.notes.append(new)
        return True

    def set_rating(self, rating: int) -> bool:
        if not rating in (Book.EXCELLENT, Book.GOOD, Book.BAD):
            return False
        self.rating = rating
        return True

    def get_notes_of_page(self, page: int) -> list[Note]:
        return [note for note in self.notes if note.page == page]

    def page_with_most_notes(self) -> int:
        pass

    def __str__(self) -> str:
        return (f"ISBN: {self.isbn}\n"
                f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Pages: {self.pages}\n"
                f"Rating: {self.rating}")


class ReadingDiary:
    def __init__(self):
        self.books: dict[str, Book] = {}

    def add_book(self, isbn: str, title: str, author: str, pages: int) -> bool:
        if not isbn in self.books:
            return False
        self.books[isbn] = Book(isbn, title, author, pages)
        return True

    def search_by_isbn(self, isbn: str) -> Book | None:
        if isbn in self.books:
            return self.books[isbn]
        return None

    def add_note_to_book(self, isbn: str, text: str, page: int, date: datetime) -> bool:
        busqueda = self.search_by_isbn(isbn)
        if busqueda is None:
            return False
        nota = Book.add_note(self.books[isbn], text, page, date)
        return nota

    def rate_book(self, isbn: str, rating: int) -> bool:
        book = self.search_by_isbn(isbn)
        if book is None:
            return False
        return book.set_rating(rating)


