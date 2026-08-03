class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_name):
        if book_name in self.books:
            print("Book already exists.")
        else:
            self.books[book_name] = "Available"
            print(f'"{book_name}" added successfully.')

    def display_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\nLibrary Books:")
        for book, status in self.books.items():
            print(f"- {book} : {status}")

    def borrow_book(self, book_name):
        if book_name not in self.books:
            print("Book not found.")
        elif self.books[book_name] == "Borrowed":
            print("Book is already borrowed.")
        else:
            self.books[book_name] = "Borrowed"
            print(f'You borrowed "{book_name}".')

    def return_book(self, book_name):
        if book_name not in self.books:
            print("Book not found.")
        elif self.books[book_name] == "Available":
            print("Book was not borrowed.")
        else:
            self.books[book_name] = "Available"
            print(f'You returned "{book_name}".')


def main():
    library = Library()

    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            book = input("Enter book name: ")
            library.add_book(book)

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            book = input("Enter book name to borrow: ")
            library.borrow_book(book)

        elif choice == "4":
            book = input("Enter book name to return: ")
            library.return_book(book)

        elif choice == "5":
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()