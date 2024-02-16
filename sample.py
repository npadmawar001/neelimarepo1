#List Demo
lcolors = ["red", 10, "green", "blue", 10.5, "red", "red45"]   #list
print(lcolors)  #one go
print(len(lcolors))
for eachcol in lcolors:
    print(eachcol)
print("eop")

#lcolors[2]="orange"         #modifying the value in list
lcolors.insert(2, "oranges")    #modifying the value in list
lcolors.append("yellow")        #inserting at last pos.
lcolors.remove("blue")                 #remove value
locolors.pop(1)

print(lcolors)  #one go


#set Demo
scolors = {"red", 10, "green", "blue", 10.5, "red", "red45"}   #list
print(scolors)  #one go

print(len(scolors))
for eachcol in scolors:
    print(eachcol)
print("eop")
scolors[2]="orange"         #modifying the value in set  - error
print(scolors)  #one go
print("eopp")


#tuple Demo
tcolors = ("red", 10, "green", "blue", 10.5, "red", "red45")  #list
print(tcolors)  #one go
print(len(tcolors))
for eachcol in tcolors:
    print(eachcol)
print("eop")

tcolors[2]="orange"         #modifying the value in tuple
print(tcolors)  #one go

print(type(lcolors))        #tuple


dcolors={
    "r": "rose",
    10:"ten",
    "or": "orange",
    "one": 1,
    "r": "red balloon",
    "fruits":["orange", "banana", "apple"],
    }


print(dcolors)
print(dcolors["r"])       # print(lcolors[2]) print(scolors[2]) print(tcolors[2])

x=dcolors["r"]        #red balloon
print(x)

dcolors["or"] = "avacodo"           #replacing a value / overriding
dcolors["p"]= "parrot"             #inserting a new k-v pair
dcolors.pop("one")

dcolors.clear()





