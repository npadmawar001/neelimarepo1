def readBooks(fpath):
    file=""
    try:
        with open(fpath, "r") as file
        fcontent=file.read()       #readlines  #readline   #rewads in one go
        return fcontent

    except FileNotFoundError:
        print("File doesn't exist")
        
    except Exception as e:
        print("Oops! and error")
    


fdata=readBooks("books.txt")
Print("Book Details:-")
print("-"*50)
print(fdata)
