# Library Management System
# Using inheritance and polymorphism

class LibraryItem:
    def __init__(self, item_id, title):
        self.item_id = item_id
        self.title = title
        self.issued = False

    def issue(self):
        if not self.issued:
            self.issued = True
            print(self.title, "has been issued.")
        else:
            print(self.title, "is already issued.")

    def return_item(self):
        if self.issued:
            self.issued = False
            print(self.title, "has been returned.")
        else:
            print(self.title, "was not issued.")

    def display(self):
        print("ID:", self.item_id)
        print("Title:", self.title)
        print("Status:", "Issued" if self.issued else "Available")


# Book class inherits LibraryItem
class Book(LibraryItem):
    def display(self):
        print("\n--- Book ---")
        super().display()


# Magazine class inherits LibraryItem
class Magazine(LibraryItem):
    def display(self):
        print("\n--- Magazine ---")
        super().display()


# Journal class inherits LibraryItem
class Journal(LibraryItem):
    def display(self):
        print("\n--- Journal ---")
        super().display()


# Creating objects
book = Book(101, "Python Programming")
magazine = Magazine(102, "Technology Today")
journal = Journal(103, "Journal of Computer Science")

# Store objects in a list
library = [book, magazine, journal]


# Display all items
print("LIBRARY ITEMS")

for item in library:
    item.display()


# Issue operations
print("\nISSUE OPERATIONS")

book.issue()
magazine.issue()


# Display updated status
print("\nUPDATED STATUS")

for item in library:
    item.display()


# Return operation
print("\nRETURN OPERATION")

book.return_item()


# Display final status
print("\nFINAL STATUS")

for item in library:
    item.display()
