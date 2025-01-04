class BaseView:
    def display_message(self, message):
        print(message)

    def display_error(self, error):
        print(f"Error: {error}")

    def display_list(self, items, title=""):
        if not items:
            print("Tidak ada data untuk ditampilkan.")
        else:
            if title:
                print(f"\n{title}")
            for idx, item in enumerate(items, 1):
                print(f"{idx}. {item}")


class BookView(BaseView):
    def display_book_details(self, book):
        print(f"Judul: {book[0]}\nPenulis: {book[1]}\nStatus: {book[2]}")
