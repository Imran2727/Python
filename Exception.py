# Exception handling
# try and except method
# try :
#     a=int(input("Enter number:"))
#     b=a+4
#     print(b)

# except Exception as e:
#     print("Error occured")
#     print("plz don't do this")
#     print(e) #To print the actual error

# 2nd example
# try :
#     a=int(input("Enter number:"))
#     b=4/a
#     print(b)

# except ValueError as e:
#     print("plz enter valid number")
#     print(e)
# except ZeroDivisionError as e:
#     print("Plz don't pass zero")
#     print(e)


#raise
# def increment(num):
#     try:
#         return int(num)+7
#     except:
#         raise ValueError("Plz enter valid number>....")

# # a=increment(10)
# a=increment("sam")
# print(a)

# try with finally
# Finally is used for default statement which print anyway
# try :
#     a=int(input("Enter number:"))
#     b=4+a
#     print(b)

# except ValueError as e:
#     print("plz enter valid number")
#     print(e)
# finally:
#     print("We r done")

# while(True):
#     print("q to exit")
#     a=input("Enter value:")
#     if(a=="q"):
#         break

#     try:
#         print("Ok...Continue")
#         a=int(a)
#         if(a>10):
#             print("Number is greater than 10")
#     except Exception as e:
#         print("Enter a valid number")
# print("Thanks for Playing ")                
