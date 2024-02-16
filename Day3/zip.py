"""
lists, tuples - multiple elements
list1 = 5
list2 = 7
"""
l1=[10,20,10,30]
l2=['red','orange','blue']
l3=['a', 'b', 'c', 'd', 'e', 'f']

zpd=zip(l1,l2)
print(list(zpd))


print(list(zip(l1,l2,l3)))
