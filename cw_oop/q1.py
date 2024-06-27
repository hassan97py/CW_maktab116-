class Book:
    def __init__(self, title, author, published_year):
        self.title = title
        self.author = author
        self.published_year = published_year

book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Published Year: {book.published_year}")