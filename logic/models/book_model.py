from config.config import Config
import os

class BaseModel:
    def __init__(self, db_file):
        self.db_file = db_file
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        os.makedirs(os.path.dirname(self.db_file), exist_ok=True)
        with open(self.db_file, 'a') as _:  # Create file if not exists
            pass


class BookModel(BaseModel):
    def __init__(self):
        super().__init__(Config.DATABASE)

    def read_books(self):
        with open(self.db_file, 'r') as f:
            return [line.strip().split(',') for line in f if line.strip()]

    def write_books(self, books):
        with open(self.db_file, 'w') as f:
            f.writelines([','.join(book) + '\n' for book in books])

    def add_book(self, title, author, status):
        with open(self.db_file, 'a') as f:
            f.write(f"{title},{author},{status}\n")

    def validate_status(self, status):
        return status in {"dipinjam", "tersedia"}
