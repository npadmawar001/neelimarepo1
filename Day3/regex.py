import re

str="""I am learning Python 3.12 for 500 hrs and the files are saved with .py extension.
I will be using python with sqlite3
"""
ptn1="Python" 
ptn2=r"\.py"  #. any char   (or) .py
ptn3=r"\d+"

#findall(pattern, string)
print(re.findall(ptn1, str))
print(re.findall(ptn1, str, re.IGNORECASE))
print(re.findall(ptn1, str, re.I))              #same as IGNORECASE
print(re.findall(ptn2, str))
print(re.findall(ptn3, str))

#compile(pattern)
ptn4=re.compile(r"\d+")
print(ptn4.findall(str))


#match(pattern, string)
ptn5=r"^I.*\d\."
print(re.match(ptn5, str))

#r"^I.*\d"   'I am learning Python 3.12 for 500'
#r"^I.*\d\." I am learning Python 3.

mtch =re.search(ptn5, str)
if mtch:
    print("Match: ", mtch.group())
    #print(mtch.group(0))
    print("Start Pos: ", mtch.start())
    print("End Pos: ", mtch.end())
    print("Span: ", mtch.span())

ptnEnd="sqlite3$"
if(re.search(ptnEnd, str)):
    print("String ends with sqlite3")


ptngrp=r"(^I\W.*am)(.*)(\d+)"
mtch =re.search(ptngrp, str)
if mtch:
    print("entire Match: ", mtch.group(0))
    print("Match as grp1: ", mtch.group(1))
    print("Match as grp2: ", mtch.group(2))
    print("Match as grp3: ", mtch.group(3)) 

mtchdList=re.split(ptn3, str)
print(mtchdList)

mtchdList1=re.split(ptn3, str, maxsplit=2)
print(mtchdList1)





