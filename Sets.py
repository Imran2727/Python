# Set-It is a collection of elements which are unordered,changeable,unindexed
# Identification-{}
# Sets doesnt store duplicte values
# a={1,2,3,4,5,5}
# print(a)
# print(type(a))

# Typecasting list and tuple into Set
# a=[1,2,3,4,5,6,7]
# c=(1,2,3,4,5,6,7)
# b=set(a) #list to set
# d=set(c) #tuple to set
# print(d)
# print(b)

# Adding any element to set
# a={"Imran","Sam",55,7}
# print(a)
# a.add(77)
# print(a)
# a.add("karl")
# print(a)

# Python prog to demonstrate frozenset and normal set
# a={"Imran","Sam",55,7}
# a.add("Sonu")
# print(a)

# a=frozenset(["Imran","Sam",55,7])
# a.add("Sonu")
# print(a)

# Adding elements using For loop
# a={"Imran","Sam",55,7}
# for i in a:
#     print(i)

# prog to do union of two sets
# a={"Imran",77,4,44.55}
# b={"Sam",77,33.1}
# c=a.union(b)
# print(c)

# Union using '|'
# c=a|b
# print(c)

# Prog for intersection of two sets
# a={"Imran","sam",33}
# b={"Imran",44,7}
# c=a.intersection(b)
# print(c)

# Intersection using '&'
# c=a&b
# print(c)

# prog to find difference in sets
# a={"Imran",44,5,7}
# b={"Sam",11,2,7,"Imran"}
# c=a.difference(b) # a-b #present in a and not in b
# d=b.difference(a) # b-a #present in b and not in a
# print(c)
# print(d)

# Clear the set and return blank set
# b={"Sam",11,2,7,"Imran"}
# b.clear()
# print(b)

# Remove an element from set
# b.remove("Sam")
# print(b)
# b.discard(7)
# print(b)