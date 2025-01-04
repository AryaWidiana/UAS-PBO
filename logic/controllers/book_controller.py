from logic.models.book_model import BookModel
from logic.views.book_view import BookView

class BookController:
    def __init__(self):
        self.model = BookModel()
        self.view = BookView()

    def add_book(self):
        title = input("Masukkan judul buku: ").strip()
        author = input("Masukkan penulis buku: ").strip()
        status = input("Masukkan status buku (tersedia/dipinjam): ").strip()

        if not self.model.validate_status(status):
            self.view.display_error("Status tidak valid. Harus 'tersedia' atau 'dipinjam'.")
            return

        self.model.add_book(title, author, status)
        self.view.display_message(f"Buku '{title}' berhasil ditambahkan!")

    def list_books(self):
        books = self.model.read_books()
        self.view.display_list([f"{book[0]} oleh {book[1]} [{book[2]}]" for book in books], "Daftar Buku")

    def update_book(self):
        books = self.model.read_books()
        self.list_books()

        try:
            book_index = int(input("Pilih nomor buku yang ingin diubah: ")) - 1

            if book_index < 0 or book_index >= len(books):
                raise ValueError

            current_book = books[book_index]
            self.view.display_book_details(current_book)

            title = input("Judul baru (kosongkan untuk tidak mengubah): ").strip() or current_book[0]
            author = input("Penulis baru (kosongkan untuk tidak mengubah): ").strip() or current_book[1]
            status = input("Status baru (tersedia/dipinjam, kosongkan untuk tidak mengubah): ").strip() or current_book[2]

            if not self.model.validate_status(status):
                self.view.display_error("Status tidak valid. Harus 'tersedia' atau 'dipinjam'.")
                return

            books[book_index] = [title, author, status]
            self.model.write_books(books)
            self.view.display_message(f"Buku '{current_book[0]}' berhasil diperbarui!")

        except ValueError:
            self.view.display_error("Nomor buku tidak valid.")

    def delete_book(self):
        books = self.model.read_books()
        self.list_books()

        try:
            book_index = int(input("Pilih nomor buku yang ingin dihapus: ")) - 1

            if book_index < 0 or book_index >= len(books):
                raise ValueError

            removed_book = books.pop(book_index)
            self.model.write_books(books)
            self.view.display_message(f"Buku '{removed_book[0]}' berhasil dihapus!")

        except ValueError:
            self.view.display_error("Nomor buku tidak valid.")

    def borrow_book(self):
        books = self.model.read_books()
        self.list_books()

        try:
            book_index = int(input("Pilih nomor buku yang ingin dipinjam: ")) - 1

            if book_index < 0 or book_index >= len(books):
                raise ValueError

            if books[book_index][2] != "tersedia":
                self.view.display_error("Buku tidak tersedia untuk dipinjam.")
                return

            books[book_index][2] = "dipinjam"
            self.model.write_books(books)
            self.view.display_message(f"Buku '{books[book_index][0]}' berhasil dipinjam!")

        except ValueError:
            self.view.display_error("Nomor buku tidak valid.")

    def return_book(self):
        books = self.model.read_books()
        self.list_books()

        try:
            book_index = int(input("Pilih nomor buku yang ingin dikembalikan: ")) - 1

            if book_index < 0 or book_index >= len(books):
                raise ValueError

            if books[book_index][2] != "dipinjam":
                self.view.display_error("Buku ini belum dipinjam.")
                return

            books[book_index][2] = "tersedia"
            self.model.write_books(books)
            self.view.display_message(f"Buku '{books[book_index][0]}' berhasil dikembalikan!")

        except ValueError:
            self.view.display_error("Nomor buku tidak valid.")
