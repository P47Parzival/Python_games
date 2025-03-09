# cinditional statments
# if, elif, else
# age = int(input("Enter you age: "))

# if(age>=18):
#     print("You are eligible to vote")
# elif(age<0):
#     print("Invalid age")
# else:
#     print("You are not eligible to vote")

# # greates number out of 4 numbers entered
# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))
# c = int(input("Enter number 3: "))
# d = int(input("Enter number 4: "))

# if(a>b and a>c and a>d):
#     print(f"a = {a} is greatest")
# elif(b>c and b>d):
#     print(f"b = {b} is greatest")
# elif(c>d):
#     print(f"c = {c} is greatest")
# else:
#     print(f"d = {d} is greatest")

# delete the spam comments
p1 = "Subscribe to my channel"
p2 = "Like the video"
p3 = "Comment below"
p4 = "Make a lot of money"

p = input("Enter your comment")
if(p1.lower() in p.lower() or p2.lower() in p.lower() or p3.lower() in p.lower() or p4.lower() in p.lower()):
    print("Spam comment")
else:
    print("Not a spam comment")