# functions 
def goodday(name):
    print(f"Good day {name}")

goodday("Dhruv")

# basic recurssion example
# def recurssion(sum):
#     # base condition
#     if (sum == 10) :
#         return sum
#     return recurssion(sum+1)

# print(recurssion(0))

# factorial
# def fact(n):
#     if(n == 1 or n == 0):
#         return 1
#     return n*fact(n-1)

# n = int(input("Enter number whose factorial is to be calculated: "))
# result = fact(n)
# print(f"The factorial of {n} is {result}")  

# recursive functions to calculate sum of first n natural numbers
def sumofn(n):
    if(n == 0):
        return n
    return n + sumofn(n-1)

n = int(input("Enter n to calculate sum of natural numbers: "))
result = sumofn(n)
print(f"Sum of {n} natural numbers is {result}")