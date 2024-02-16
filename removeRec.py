#copyting the file based on some filteration
"""
with open("books.txt", "r") as f1:
    with open("filteredbook.txt", "w") as f2:
        for eachline in f1:
            if "Yashwant" not in eachline:
                f2.write(eachline)
"""

#remove the unwanted lines

def removeBook(fpath):
    with open("books.txt", "r") as f:
        lines=f.readlines()
        print(lines)
        print(type(lines))
        #creating a list of only wantedLines
        wantedLines=[eachline for eachline in lines if "Yashwant" not in eachline]
        
    with open("books.txt", "w") as f:
        f.writelines(wantedLines)
    

removeBook("books.txt")
