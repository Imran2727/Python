# Q.1-What is statement in python?
# Ans-Any instruction written in the source code and executed by the Python interpreter is called a statement.
#     such as-print("IMRAN")

# Q.2-Difference between call by value and call by reference?
# Ans- Immutable objects passed as arguments in a function are referred as in Call by Value,
#      where copy of variable is passed and Mutable objects, when passed as arguments 
#      are referred to as Call by Reference where value of variable itself gets changed.

# Q.3-Is Integer mutable or not?
# Ans-Not..Int is an immutable data type.

# Q.4-Difference between tuple and list?
# Ans-The primary difference between tuples and lists is that tuples are immutable as opposed to lists which are mutable.
#     Lists are denoted by [] and tuple by ().

# Q.5-What is isalnum() and isdigit() in string?
# Ans-The isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers).
#     If not, it returns False
# string contains either alphabet or number 
# name1 = "Python3"
# print(name1.isalnum()) #True
# # string contains whitespace
# name2 = "Python 3"
# print(name2.isalnum()) #False

# Whereas the isdigit() method returns True if all char in string are digits else returns false.
# str1 = '342'
# print(str1.isdigit()) #True
# str2 = 'python'
# print(str2.isdigit()) #False