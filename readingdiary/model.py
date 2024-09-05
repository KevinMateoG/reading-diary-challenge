from datetime import datetime


# TODO: Add code here
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
        else:
            new = Note(text, page, date)
            self.notes.append(new) #correccion - agregado
            return True

    def set_rating(self, rating: int) -> bool:
        #if rating == Book.EXCELLENT or Book.GOOD or Book.BAD:
        if rating not in (Book.EXCELLENT, Book.GOOD, Book.BAD): #correccion
            return False
        else:
            self.rating = rating
            return True

    def get_notes_of_page(self, page: int) -> list[Note]:
        #agregado - compleatado por hacer pass
        return [note for note in self.notes if note.page == page]

    def page_with_most_notes(self) -> int:
        # agregado - compleatado por hacer pass
        #forma: 1
        pages = [note.page for note in self.notes]
        lista = []
        if pages == []:
            return -1

        else:
            notes=  {}
            for page in pages:
                if page not in notes:
                    notes[page] = 1
                else:
                    notes[page] += 1
            page = -1
            moste_count = 0
            for key in notes:
                if notes[key] > moste_count:
                    moste_count = notes[key]
                    page = key
            return page
            #return max(set(pages), key=pages.count)

    def __str__(self) -> str:
        """if self.rating == 3:
            self.rating = "excellent"
        elif self.rating == 2:
            self.rating = "good"
        elif self.rating == 1:
            self.rating = "bad"
        elif self.rating == -1:
            self.rating = "unrated"""
        dec = {3: "excellent",
               2: "good",
               1:"bad",
               -1:"unrated"
        }

        return f"ISBN: {self.isbn}\n Title: {self.title}\n Author: {self.author}\n Pages: {self.pages}\n Rating: {dec[self.rating]}"


class ReadingDiary:
    def __init__(self):
        self.books: dict[str, Book] = {}

    def add_book(self, isbn: str, title: str, author: str, pages: int) -> bool:
        if isbn in self.books:
            return False
        else:
            new = Book(isbn, title, author, pages)
            self.books[isbn] = new
            return True

    def search_by_isbn(self, isbn: str) -> Book | None:
        """if isbn in Book:
            return isbn
        else:
            return None"""
        return self.books.get(isbn)

    def add_note_to_book(self, isbn: str, text: str, page: int, date: datetime) -> bool:
        book = self.search_by_isbn(isbn)
        if not book:
            return False

        return book.add_note(text, page, date)

