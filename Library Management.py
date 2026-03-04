#Library Management System

class Book:
    
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.__isbn = isbn
        self.is_availaible = True

    def get_isbn(self):
        return self.__isbn
        

    def __str__(self):
        return f"Book is {self.is_availaible}, Title is {self.title}, Author is {self.author}, ISBN is {self.__isbn}"

class Library:
    def __init__(self):
        self.book_list = []
    def add_book(self,new_book):
        self.book_list.append(new_book)
    def show_books(self):
        return f"Book are {self.book_list}"
    
    def borrow_book(self,book_name):
        self.book_name = book_name
        if self.book_name in self.book_list:
            self.is_availaible = False
            print("Book is  availaible")
        
        else:
            print("Oh! Book is not availaible")


b = Book("python","xyz",123)
print(b)

a = Library()
a.add_book("python")
a.add_book("java")
print(a.show_books())
print(a.borrow_book("java"))
print(a.borrow_book("c++"))





