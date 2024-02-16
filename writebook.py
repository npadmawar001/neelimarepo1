# remove books by Yashwant
# write
# append

def addNewBook(fpath, newBook):
    try:
        with open(fpath, "w") as file:
            for key, val in newBook.items():
                file.write(f"{key}:{val}\n")
        print("new book is written into file")
    except Exception as e:
        print("Oops! and error", e)  

b1="Python | Rossum | 500 | 2000"
b2="""Python1 | Rossum | 500 | 2000\n
Python2 | Rossum |     | 2000\n
Python3 | Rossum | 500 | 2000\n
Python4 | Rossum | 500 | 2000\n
"""
bdict={"bid":101, "bname":"C program", "bauthor":"DR", "bprice":200.50}
addNewBook("book1.txt", bdict)


