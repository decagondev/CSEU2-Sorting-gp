from book import Book

def insertion_sort(books):
    # loop through len - 1 elements
    for i in range(1, len(books)):
        temp = books[i]
        j = i
        while j > 0 and temp.genre < books[j - 1]. genre:
            # shift left until correct genre is found
            books[j] = books[j - 1]
            j -= 1
        books[j] = temp
    return books

b1 = Book("f", "f", "f")
b2 = Book("e", "e", "e")
b3 = Book("d", "d", "d")
b4 = Book("c", "c", "c")
b5 = Book("b", "b", "b")
b6 = Book("a", "a", "a")
books = [b1, b2, b3, b5, b4, b6]
print(books)

sorted_books = insertion_sort(books)
print("--------------------")
print(sorted_books)