class Book:
    _library = []
    def __init__(self, title, author, published_year):
        self.title = title
        self.author = author
        self.published_year = published_year

book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
Book._library = 'local'
print(book._library)