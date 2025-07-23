class Library:
    def __init__(self):
        self.books = {
            "The Alchemist": True,
            "Harry Potter": True,
            "Atomic Habits": True,
            "Clean Code": True,
            "Deep Work": True
        }

    def viewAll(self):
        for book in self.books:
            status = "Available" if self.books[book] else "Borrowed"
            print(f"{book}: ({status})")

    def borrowBook(self, book):
        if book in self.books and self.books[book]:
            self.books[book] = False
            print("Borrowed " + book)
        else:
            print("No such book found")

    def returnBook(self, book):
        if book in self.books:
            if self.books[book]:
                print("You haven't borrowed " + book + "yet")
            else:
                self.books[book] = True
                print("Returned " + book)
        else:
            print("No such book found")

    def addBook(self, book):
        if book in self.books:
            print("Cannot add " + book + " again")
        else:
            self.books[book] = True
            print("Added " + book)

def main():
    lib = Library()

    print("Welcome to EXL Library")

    while True:
        print("\n===== Library Menu =====")
        print("Choose an option:")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Add Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            lib.viewAll()
        elif choice == '2':
            book = input("Enter the name of the book you want to borrow: ")
            lib.borrowBook(book)
        elif choice == '3':
            book= input("Enter the name of the book you want to return: ")
            lib.returnBook(book)
        elif choice == '4':
            book = input("Enter the name of the book you want to add: ")
            lib.addBook(book)
        elif choice == '5':
            print("Thanks for visiting EXL Library")
            break
        else:
            print("Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()