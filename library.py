class Library:
    def __init__(self, bookslist, name):
        self.bookslist = bookslist
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have the following books in our library: {self.name}")
        for book in self.bookslist:
            print(book)

    def lendBook(self, book, user):
        if book in self.bookslist:
            if book not in self.lendDict.keys():
                self.lendDict.update({book: user})
                print("Book has been lent. Database updated.")
            else:
                print(f"Book is already being used by {self.lendDict[book]}")
        else:
            print("Apologies! We don't have this book in our library.")

    def addBook(self, book):
        if book in self.bookslist:
            print("Book already exists.")
        else:
            self.bookslist.append(book)
            print("Book added.")

    def returnBook(self, book):
        if book in self.lendDict.keys():
            self.lendDict.pop(book)
            print("Book returned successfully.")
        else:
            print("The book does not exist in our lending database.")


def main():
    library = Library(["Python Basics", "Networking 101", "Hacking Tricks"], "Cyber Library")
    
    while True:
        print("\nWelcome to our library. Following are the options:")
        print("""
        1. Display Books
        2. Lend a Book
        3. Add a Book
        4. Return a Book
        """)

        userinput = input("Press Q to quit or C to continue: ")

        if userinput.lower() == 'c':
            try:
                userchoice = int(input("Select the option number: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if userchoice == 1:
                library.displayBooks()

            elif userchoice == 2:
                book = input("Enter book name you want to lend: ")
                user = input("Enter your name: ")
                library.lendBook(book, user)

            elif userchoice == 3:
                book = input("Enter book name you want to add: ")
                library.addBook(book)

            elif userchoice == 4:
                book = input("Enter the name of the book you want to return: ")
                library.returnBook(book)

            else:
                print("Please choose a valid option.")

        elif userinput.lower() == 'q':
            print("Thanks for using the library!")
            break

        else:
            print("Please enter a valid option.")



main()
