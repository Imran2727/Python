# Identification=[square brackets]
# List is data type where we store multiple elements
# It is mutable data type
# Indexing starts with 0 and length from 1

# List=[1,2,"Imran","7"]
# print(List)
# print(type(List))

# # Update
# List[3]="Sam"
# print(List)

# Task1
# a=["Sam",690,"Kriti",89.98,"Rahul"]
# b=a[0]
# print(b[2]) or print(a[0][2])

# # Task2
# print(a[1:4])

# # Task3
# a[1]=444
# print(a)

# Methods in Lists
# 1.Min- Gives minimum value present in list
# a=[1,2,3,4,5]
# print(min(a))
# x=["imran","simran"]
# print(min(x))
# b=["imran","Shyam"]
# print(min(b)) #Gives "Shyam" bcoz ASCII value of "S" is less in Uppercase letter

# 2.Max-Gives the maximum value in list
# a=[1,2,3,4,5]
# print(max(a))
# x=["imran","simran"]
# print(max(x))
# b=["imran","Shyam"]
# print(max(b)) #Gives "imran" bcoz ASCII value of "i" is more in lowercase

# 3.Index-Gives the index of given element
# syntax-ListName.index(value)
# a=["sam",33,"222","rahul"]
# print(a.index(33))

# 4.Append-Adds element to last of the List.
# syntax-ListName.append(value)
# a=["sam",33,"222","rahul"]
# a.append("Loki")
# print(a)

# For user defined list append
# a=[]
# for i in range(5):
#     x=int(input("Enter ur value"))
#     a.append(x)
# print(a)

# 5.Count-It is used to count the frequency of the element in given List.
# syntax-ListName.count(value)
# a=["sam",33,7,"222",7,"rahul"]
# x=a.count(7)
# print("Count is:",x)

# a=[]
# for i in range(5):
#     x=(input("Enter ur value"))
#     a.append(x)
# print(a)
# y=input("Enter the item whose count u want:")
# z=a.count(y)
# print("The count is:",z)

# 6.Insert-Inserts the desired element into the list at the given index
# syntax-ListName.Insert(Index,value)
# a=[1,2,3,4,5]
# a.insert(0,"Imran")
# print(a)

# a=[]
# for i in range(4):
#     x=(input("Enter the value: "))
#     a.append(x)
# print(a)
# p=int(input("Enter ur index: "))
# q=(input("Enter ur value to insert at given index:"))
# a.insert(p,q)
# print(a)

# 7.Remove-It is used to delete the desired element from given list.If has duplicate values then removes 1st occurance.
# syntax-ListName.Remove(value)
# a=["pizza","burger","momos"]
# a.remove("pizza")
# print(a)
# a=["pizza","burger","momos","pizza"]
# a.remove("pizza")
# print(a)

# a=[]
# for i in range(4):
#     x=(input("Enter the value: "))
#     a.append(x)
# print(a)
# x=input("Enter the element to be removed: ")
# a.remove(x)
# print(a)

# 8.Reverse-reverses the given list 
# syntax-ListName.reverse
# a=["pizza","burger","momos","french fries"]
# a.reverse()
# print(a)

# a=[]
# for i in range(4):
#     x=(input("Enter the value: "))
#     a.append(x)
# print(a)
# a.reverse()
# print(a)

# 9.Pop-deletes last element of the list
# syntax-ListName.Pop
# a=["pizza","burger","momos","french fries"]
# a.pop()
# print(a)
# a.pop()
# print(a)

# Program to find the sum of all elements in list
# a=[]
# len=int(input("Enter the size"))
# for i in range(len):
#     x=int(input("Enter the values:"))
#     a.append(x)
# print(a)
# sum=0
# for i in range(len):
#     sum=sum+a[i]
# print("Sumof all elements:",sum)

# Program to find max and 2nd max number in user defined list

# a=[]
# len=int(input("Enter the size:"))
# for i in range(len):
#     x=int(input("Enter the values:"))
#     a.append(x)
# print(a)
# print("Maximum number is:",max(a))
# a.remove(max(a))
# print(a)
# print("2nd maximum number is:",max(a))

# Program to find square of elements in user defined list
# a=[]
# len=int(input("Enter the size:"))
# for i in range(len):
#     x=int(input("Enter the values:"))
#     a.append(x)
# print(a)

# square=list(map(lambda x:x*x, a))
# print("The square of elements is:",square)

# Program to find total number of even and odd number in list
# a=[]
# len=int(input("Enter the size:"))
# for i in range(len):
#     x=int(input("Enter the values:"))
#     a.append(x)
# print(a)
# even=0
# odd=0
# for i in range(len):
#     if(a[i]%2==0):
#          even=even+1
#     else:
#          odd=odd+1
# print("The total even numbers are:",even)
# print("The total number of odd are:",odd)    

# Prog to find min and 2nd min num in list
# a=[]
# len=int(input("Enter the size:"))
# for i in range(len):
#     x=int(input("Enter the values:"))
#     a.append(x)
# print(a)
# print("Minimum number is:",min(a))
# a.remove(min(a))
# print(a)
# print("2nd minimum number is:",min(a))

# Prog to seperate even and odd from list
# a=[]
# len=int(input("Enter the size:"))
# for i in range(len):
#     x=int(input("Enter the values:"))
#     a.append(x)
# print(a)
# Even_List=[]
# Odd_List=[]
# for i in range(len):
#     if(a[i]%2==0):
#         Even_List.append(a[i])
#     else:
#         Odd_List.append(a[i])
# print("Even numbers are:",Even_List)
# print("Odd numbers are:",Odd_List)        
