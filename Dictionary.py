# Dictionary-It is a collection of elements which are unordered and changeable and unindexed.
# Identification-{Curly brackets} which include keys and values.

# a={1:"Imran",
#    2:"Sam",
#    3:55,
#    "year":2023}
# print(a)
# print(type(a))

# Accessing the dictionary
# we can access the contents of dictionary by referring to its keyname inside square brackets
# a={"Name":"Imran",
#    "Lang":"Python",
#    "Dept":"IT"
#    }
# print(a)
# print(a["Name"])

# Changing the values of dictonary
# a={"Name":"Imran",
#    "Lang":"Python",
#    "Dept":"IT"
#    }
# a["Name"]="Sam"
# print(a)

# a={"Name":"Imran",
#    "Lang":"Python",
#    "Dept":"IT"
#    }
# To print all keys
# for i in a:
#     print(i)
# # To print all values
# for i in a:
#     print(a[i])


# To print all keys
# for i in a.keys():
#     print(i)
# # To print all values
# for i in a.values():
#     print(i)
# # To print all keys and values pair
# for i in a.items():
#     print(i)

# Check whether the key is available in dicionary or not
# if "Name" in a:
#     print("Yes")
# else:
#     print("no")

# adding a key value pair in dict
# a["Salary"]=50000
# print(a)

# New_Dict={
#     "Brand":"Apple",
#     "Name":"Iphone 13 pro",
#     "Price":125000
#     }
# print(New_Dict)
# for i in New_Dict.values():
#     print(i)
# New_Dict["Storage"]="in GB"
# print(New_Dict)

# Methods in Dictionary-
# 1.Len-Gives length of dict or keys
# a={"Name":"Imran",
#    "Lang":"Python",
#    "Dept":"IT"
#    }
# print(len(a))

# 2.Pop-Removes element from last of dict
# a={"Name":"Imran",
#    "Lang":"Python",
#    "Dept":"IT"
#    }
# a.pop("Dept")
# print(a)

# 3.PopItem-Removes last key value pair from the dict
# a={"Name":"Imran",
#    "Lang":"Python",
#    "Dept":"IT"
#    }
# a.popitem()
# print(a)

# 4.Del-Deletes the key and its value
# a={"Name":"Imran",
#    "Lang":"Python",
#    "Dept":"IT"
#    }
# To delete single key
# del a["Dept"]
# print(a)
# del a #To delete whole Dictionary
# print(a)

# 5.Clear-Clears all the key value pairs and gives blank dict
# a={"Name":"Imran",
#    "Lang":"Python",
#    "Dept":"IT"
#    }
# a.clear()
# print(a)

# 6.Get-To get the desired value by passing key
# a={"Name":"Imran",
#    "Lang":"Python",
#    "Dept":"IT"
#    }
# b=a.get("Name")
# print(b)   

# 7.Copy-Creates a copy of dict 
# a={"Name":"Imran",
#    "Lang":"Python",
#    "Dept":"IT"
#    }
# b=a.copy()
# b["Name"]="Sam" #when changes are made copy is changes original dict stays same
# print(b)

# 8.Fromkeys-assigns given value to all the keys
# a=("a","b","c")
# b=1
# c=dict.fromkeys(a,b)
# print(c)

# 9.Setdefault-add desired key value pair
# a={"Name":"Imran",
#    "Lang":"Python",
#    "Dept":"IT"
#    }
# a.setdefault("Year",2023)
# print(a)

# 10.update-Updates the value of dict
# a={"Name":"Imran",
#    "Lang":"Python",
#    "Dept":"IT"
#    }
# a.update({"Dept":"Mech"})
# print(a)

# To concatenate and follow dict and create a new one
# a={1:"Sam"}
# b={2:"Imran"}
# c={3:77}
# d={}
# for i in (a,b,c):d.update(i)
# print(d)