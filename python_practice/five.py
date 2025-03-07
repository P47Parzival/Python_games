# Dictionary
# dictionary is collection of key value pairs, it is mutable
# here indexing does work you have to use key 
marks = {
    "Dhruv": 100,
    "Dhula": 99,
    "Mali": 98,
    0: "Dhruv"
}

print(marks)
print(marks["Dhula"])
print(len(marks))
print(marks.items())       #will list out everything in dictionary
print(marks.keys())        #will list out all the keys
print(marks.values())      #will list out all the values
marks.update({"Dhruv": 95})    #updating the value of key Dhruv
marks.pop("Mali")       #removing the key Mali
print(marks.get("Dhruv1"))   #will return the value of key Dhruv(hers the catch if you do marks["Dhruv1"] it will return error but get will return none)



# Sets in python
# set is collection of non repetetive elements and set are unindexed 
# collection of well defined objects
# empty set is fromed like these
empty_set = set()
set = {1, 3, 34, 3, 4, 43, 34, "Dhruv"}
print(set)

# some functions of set
# set.sort()  #will return error as set is not subscriptable
set.add("Dhula")
# set.pop()    #removes random element
set.remove(3)   #removes the element here 3 is value not index
print(set)


# set union intersection
set1 = {1, 3, 4, 5, 6}
set2 = {3, 4, 5, 6, 7}
print(set1.issubset(set2))      #returns true or false
print(set1.union(set2))
print(set1.intersection(set2))