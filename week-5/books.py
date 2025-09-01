class Genre:
    def __init__(self, name: str):
        if not name:
            raise ValueError("Genre name cannot be empty")
        self.name = name

    def __str__(self):
        return self.name


class Book:
    def __init__(self, title: str, year: int, genres=None):
        if not title:
            raise ValueError("Title cannot be empty")
        self.title = title
        self.year = year
        self.genres = genres if genres else []

    def add_genre(self, genre: Genre):
        if genre not in self.genres:
            self.genres.append(genre)

    def remove_genre(self, genre: Genre):
        if genre in self.genres:
            self.genres.remove(genre)

    def display_info(self):
        genres_str = ", ".join([str(g) for g in self.genres]) if self.genres else "None"
        print(f"Title: {self.title}, Year: {self.year}, Genres: {genres_str}")


class Librarian:
    def __init__(self, name: str):
        self.name = name

    def add_genre_to_book(self, book: Book, genre: Genre):
        book.add_genre(genre)
        print(f"Librarian {self.name} added genre '{genre}' to book '{book.title}'.")

    def remove_genre_from_book(self, book: Book, genre: Genre):
        book.remove_genre(genre)
        print(f"Librarian {self.name} removed genre '{genre}' from book '{book.title}'.")


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library '{self.name}'.")

    def list_books(self, librarian: Librarian):
        print(f"\nBooks in the library '{self.name}', managed by {librarian.name}:")
        if not self.books:
            print(" No books found.")
        for book in self.books:
            book.display_info()
