# string is immutable(once it is formed cannot be changed)
name = 'Dhruv'

# string slicing
print(len(name)) #length of string 
nameshort = name[0:3]       #here 0 is starting index and 3(exclude) is ending index
print(nameshort)

# slice with skip value 
newname = 'abcdefghijk'
nameskip = newname[0:4:2]   #here first newname[0:4] is printed and then 2 is skiped and then next element is printed
print(nameskip)

# some functions 
# sample = 'hello world'
# print(sample.endswith('d'))  
# print(sample.count('o'))
# print(sample.upper())
# print(sample.lower())
# print(sample.replace("hello", "hi"))
# print(sample.find('o'))
# print(sample.split(' '))    #split the string by space
# print(sample.capitalize())
# print(sample.title())

# escape sequence characters
# print('hello\nworld')
# print('hello\tworld')
# print('hello\\world')

# new feature of python 
# f string
# samplename = input("Enter your name:")
# print(f"AYO! {samplename}")

# fill calendername and date
# calendername = input("Enter name of calender:")
# date = input("Enter date")
# print(f"Name of calender is {calendername} and date is {date}")

# detect double spaces in a string 
samplestring = "Hello world  world"
print(samplestring.count("  "))
print(samplestring.replace("  ", " "))