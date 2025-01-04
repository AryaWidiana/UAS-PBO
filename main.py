from logic.controllers.book_controller import BookController


def main():
    controller = BookController()

    menu = {
        "1": ("Tambah Buku", controller.add_book),
        "2": ("Lihat Daftar Buku", controller.list_books),
        "3": ("Ubah Buku", controller.update_book),
        "4": ("Pinjam Buku", controller.borrow_book),
        "5": ("Kembalikan Buku", controller.return_book),
        "6": ("Hapus Buku", controller.delete_book),
        "7": ("Keluar", None)
    }

    while True:
        print("\nSistem Manajemen Buku")
        for key, (desc, _) in menu.items():
            print(f"{key}. {desc}")

        choice = input("Pilih menu: ").strip()
        if choice in menu:
            action = menu[choice][1]
            if action:
                action()
            else:
                print("Keluar dari program.")
                break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
