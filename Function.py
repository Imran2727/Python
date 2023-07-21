# def Addition():
#     a=int(input("Enter value:"))
#     b=int(input("Enter value:"))
#     c=a+b
#     print("Addition of given value is:",c)

# Addition()

# def Addition():
#     a=(input("Enter value:"))
#     b=(input("Enter value:"))
#     c=a+b
#     print("Addition of given string is:",c)

# Addition()

# Function with passing arguments and parameters

# def add(a,b):
#     c=a+b
#     print("Addition is:",c)
# p=int(input("Enter 1st para:"))
# q=int(input("Enter 2nd para:"))
    
# add(p,q)

# def print_func(a,b):
#     while(a<=b):
#         print(a)
#         a=a+1
# p=int(input("Enter value:"))
# q=int(input("Enter value:"))

# print_func(p,q)

# def checkno():
#     a=int(input("Enter no: "))
#     if(a%2==0):
#         print("Even")
#     else:
#         print("Odd")

# checkno()

# with para and arg

# def checkno(a):

#     if(a%2==0):
#         print("Even")
#     else:
#         print("Odd")
# i=int(input("Enter no: "))

# checkno(i)

# Function with no arguments and no return type

# def add():
#     a=10
#     b=11
#     c=a+b
#     print("Addition is:",c)

# add()

# # Function with arguments and no return type
# def add(a,b):
    
#     c=a+b
#     print("Addition is:",c)
# a=11
# b=15

# add(a,b)

# sum=0
# a=int(input("Enter value"))
# while(a>0):
#     sum=sum+(a%10)**2
#     a=a//10
# print("The sum of square is:",sum)


# i=int(input("Enter value:"))
# while(i>0):
#     if(i%2==0):
#         print("Even")
#     else:
#         print("odd")
#     i=i+1

# lambda Function
# The lambda function takes multiple parameters and gives output of expression 
# Single argument
# x=lambda a:a+8
# print("The total is:",x(4))

# # Multiple arguments
# x=lambda a,b:a*b
# print("Multiplication is:",x(10,7))

# x=lambda a,b,c:a+b-c
# print("The total is:",x(10,20,4))

# x=lambda a,b:a-b
# print("The value of equation is :",x(int(input("Enter value:"))
#                                     ,int(input("Enter value:"))))

# Filter function
# it filters the value given by the condition in the function

# a=[11,22,33,44,55]
# def func(x):
#     if(x<60):
#         return True
#     else:
#         return False

# q=list(filter(func,a))
# print("filtered=",q)

# Map function
# It executes specified function for each item in iterable

# a=["22","11","33"]
# for i in range(len(a)):
#     a[i]=int(a[i])
# print(a)

# x=list(map(int,a))
# print(x)

# Example2

# a=[1,2,3,4]
# def sqre(a):
#     a*a
# square=list(map(sqre,x))
# print(square)

# square=list(map(lambda x:x*x, a))
# print(square)

# Reduce function

# from functools import reduce
# val=[10,11,12,13]
# def my_func(a,b):
#     return a+b
# add =reduce(my_func,val)
# print(add)