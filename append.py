# remove books by Yashwant
# write
# append

def addNewBook(fpath, newBook):
    try:
        with open(fpath, "a") as file:
            file.write(newBook)
        print("new book is written into file")
    except Exception as e:
        print("Oops! and error", e)  

b1="Python | Rossum | 500 | 2000"
b2="""Python1 | Rossum | 500 | 2000\n
Python2 | Rossum |     | 2000\n
Python3 | Rossum | 500 | 2000\n
Python4 | Rossum | 500 | 2000\n
"""
addNewBook("book1.txt", b2)


