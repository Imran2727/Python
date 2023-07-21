# Tuple-It is a collection of elements which are ordered and unchangeable or immutable.
# Identification=(round brackets)
# indexing starts from 0 and length starts from 1.

# a=(1,2,"Imran",55.44)
# print(type(a))
# a=("Sam") #if single value then its data type is given
# print(type(a))
# a=("Sam",) #if comma or multiple values then tuple

# The tuple is an immutale data type..hence to make changes in tuple we have to type cast it into list and make changes.
# a=(1,2,"Imran",55.44)
# b=list(a)
# b[1]="Sam"
# print(b)
# c=tuple(b)

# Creating tuple from existing sequence
# a=tuple("Sam")
# print(a)

#Traversing the tuple
# a=("Imran",3,5,"Sam",7)
# # Method 1
# for i in a:
#     print(i)
# # Method 2 
# for i in range(len(a)):
#     print(a[i])

# Concatenating tuple
# a=(1,2,3,4)
# b=(5,6,7)
# c=a+b
# print(c)

# Replication in tuple
# a=(1,2,34,56)
# b=a*2
# print(b)

# Slicing in tuple-Same as list slicing
# a=(1,2,3,4,5,6,7)
# # print(a[1:4])
# print(a[1:6:2]) #[Start_value:Last_value+1:Step_value]

# a=[]
# len=int(input("Enter the size:"))
# for i in range(len):
#     x=int(input("Enter the values:"))
#     a.append(x)
# print(a)
# b=tuple(a)
# c=b[2:5]
# print(c)

# a=()
# print(type(a))
# b=list(a)
# print(type(b))
# b[0]=("Enter ur value:")
# b[1]=("Enter ur value:")
# b[2]=("Enter ur value:")
# c=tuple(b)
# print(c)

# Methods in tuple-
# 1.len-Gives length of tuple 
# a=(1,2,3,4,5,6,7)
# print(len(a))

# 2.Min-Gives minimum value in tuple
# a=(1,2,3,4,5,6,7)
# print(min(a))

# 3.Max-Gives maximum value in tuple
# a=(1,2,3,4,5,6,7)
# print(max(a))

# 4.Index-Gives the index of desired element in tuple
# syntax-tupleName.index(Value)
# a=("Imran","Sam",55,4)
# print(a.index(4))

# 5.Count-Gives the count of the desired element in tuple
# syntax-tupleName.count(Value)
# a=("Sam",33,44,55,33,55,55)
# print(a.count(33))

# Casting dictionary into tuple
# type casting gives keys into tuple
# Dict={1:"imran",
#       2:"Sam",
#       3:3}
# a=tuple(Dict)
# print(a)

# Tuple manipulation-
# 1.To change values-
# Type cast the given tuple into list then change values by index and then recast into the tuple.

# 2.To check whether the element is present in tuple or not 
# a=("sam","Imran",44)
# if "Imran" in a:
#     print("Element is present")
# else:
#     print("Element is not present")
