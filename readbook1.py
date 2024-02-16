# first row in capitalcase
# Author names in capital case : eachline -> list=split(|) list[1]-convert upper
# padding of the details
# display unique authors - convertign into a set

def readBooks(fpath):
    file=""
    authors=""
    paddedword=""
    print("Book Details:-")
    print("-"*50)

    try:
        with open(fpath, "r") as file:
            line1=True                      #flag for the first line
            for eachline in file:
                if line1:                       #truified for the first time
                    eachline=eachline.upper()   
                    line1=False
                lwords=eachline.split('|')
                eachline=""
                for ew in range(len(lwords)):
                    if ew==1:
                        authors=authors+lwords[ew]+","      #  string authors
                        lwords[ew]=lwords[ew].upper()
                    paddedword = lwords[ew].ljust(30)
                    eachline=eachline+paddedword                    
                print(eachline)
                lauthors=authors.split(",")                 #list of authors
                sauthors =set(lauthors[1:len(lauthors)-1])
        #print(authors)      #same as lauthor values
        print(lauthors)
        print(sauthors)

    except FileNotFoundError:
        print("File doesn't exist")
        
    except Exception as e:
        print("Oops! and error", e)  

readBooks("books.txt")


