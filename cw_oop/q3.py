class Book:
    def __init__(self, title, author, published_year):
        self.title = title
        self.author = author
        self.published_year = published_year

    def summary(self):
        return self.title, self.author, self.published_year

book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
print(book.author)

res = book.summary()
print(res)