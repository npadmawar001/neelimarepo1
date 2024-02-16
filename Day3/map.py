"""
map als oworkso niterables like filter
res in the form of map object
some sort of TRANSFORMATION : T/F,,,     uppercase, etc.
"""

num=[10,20,10, 15, 5, 30]
maxRes=list(map(lambda en:en>10, num))
print(maxRes)
#[False, True, False, True, False, True]

fruits=['guava','orange','avacado','banana','apple']
#fruits_f=list(map(lambda ef: ef.upper(), fruits))
fruits_f=list(map(str.upper, fruits))
print(fruits_f)


