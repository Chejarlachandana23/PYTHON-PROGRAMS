class Book:
    def __init__(self,title):
        self.title=title
def create_book_list():
        return[Book("Python 101"),Book("AI Basics"),Book("Data Science")]
Books=create_book_list()
for b in Books:
    print("Book Title:",b.title)


