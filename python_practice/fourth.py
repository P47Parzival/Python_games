# lists
# list are mutable unlike strings which are not 
# list are collection of items and can be of any type

list1 = ["Dhruv", "Apple", 2.1234, 12, True]
list1[2] = 3.14
print(list1)

# some functions of list
list1.append("Dhula")
list1.pop() #removes last element
list1.insert(2, "Mali") #inserting at particular index
list1.remove("Apple")   #removing element
list1.reverse()
print(list1)

list2 = [8, 2, 6, 3, 9]
list2.sort()    #sorts the list but the catch is it should be of same data type 
print(list2)


# tuples
# tuples are immutable unlike list which are mutable 
a = (1, 2, 3, True, "Dhruv", 3, 3.14)
# a = (1,)   #single element tuple
print(type(a))

# some funtions of tuple
print(a.count(3))   #counts the number of times 3 is present in tuple
print(a.index(3))   #returns the index of first occurence of 3

# # returns the second occurrence of 3
# c = a.index(3)
# print(c)
# d = a[c+1:len(a)]
# print(d)
# e = d.index(3)
# print(e)
# f = c + e + 1
# print(f)

# conctenation of tuple
tupl1 = (1, 2, 3)
tupl2 = (4, 5, 6)
tupl3 = tupl1 + tupl2
print(tupl3)
# repeating tuple
tupl4 = tupl1 * 3       #repeats the tuple 3 times
print(tupl4)
# chenck item in tuple using in keyword
print(3 in tupl1)

# print 2 fruits name entered by user
fruits = []
f1 = input("Enter fruit 1: ")
f2 = input("Enter fruit 2: ")
fruits.append(f1)
fruits.append(f2)
print(fruits)