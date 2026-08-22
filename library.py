"""
Problem:  Create Library Management System

Sample Input : User define

Platform: SelfStudy

Difficulty: hard

"""

class Library():
     def __init__(self):
          print("A new Library has been Created...!")

          no_of_books = 0
          books = []

          self.no_of_books = no_of_books
          self.books = books


     def show_books(self):
          return self.books
     

     def add_books(self , book):
          self.books.append(book)
          self.no_of_books += 1

     def show_number_of_books(self):
          return self.no_of_books


library = Library()
library.add_books("Book 1")
library.add_books("Book 2")

library.show_books()
library.show_number_of_books()