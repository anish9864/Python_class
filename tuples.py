name = ("ram", "shyam", "hari", "ram")



#1st way to change tuple is to convert in list and list to tuples

# name.remove("mohan") #cannot change the value of tuple
# name.append("Sita")
# new_name = list(name)
# new_name.append("Sita")
# new_name2 = tuple(new_name)
# print(new_name2)

# new_name = list(name)
# new_name.remove("ram")
# new_name2 = tuple(new_name)
# print(new_name2) #Removes only first ram

#2nd way is tuples tuples add/extend

# surname = ("gupta", "sharma", "verma", "gupta")
# name = name + surname
# print(name)


# entire tuple can be deleted but not the individual data inside tuple
# surname = ("gupta","adhikari")
# del surname
# print(name)
# print(surname) #says 'surname' is not defined as it is deleted


#unpackingvalues from tuples
# email = ("aaditya@gmail.com","anish@gmail.com","ashim@gmail.com") 
# (aaditya,anish,ashim) = email  #unpacking values from tuples
# print(aaditya)
# print(anish)
# print(ashim) #can use any variables instead of names


#unpacking values from tuples(using astrick *)
# email = ("aaditya@gmail.com","anish@gmail.com","ashim@gmail.com", "meghan@gmail.com","rojit@gmail.com") 
# (aaditya,*anish,ashim) = email  #unpacking values from tuples(using astrick *)
# print(aaditya)
# print(anish)
# print(ashim)



# #Data replication inside tuples
# name = ("Ram","Shyam")
# name = name * 3 #Data replication inside tuples
# print(name)


"""
Lists vs Tuples:
List: 
ordered, changeable, allows duplicate members., syntax [], methods are available, accessing the value is slow, data are not secured as compared to tuples
Tuple:
ordered, unchangeable, allows duplicate members. syntax (), methods are not available, accessing the value is fast, data are secured here than list
Set:
unordered, unchangeable, doesn't allow duplicate members, syntax {}, methods are available only for adding or removing data, 
Dictionary: 
ordered/unordered , changeable, doesn't allow duplicate members,  syntax = {}, methods are available 
"""