#python program to find even or odd
#using modulo operator "%"
num=int(input("Enter your number: "))
if num%2==0:
    print("It is even!")
else:
    print("It is odd!")
#using Bitwise AND operator(&)
"""Here is a simple program to check whether a number is even or odd using bitwise AND operator(&)
The bitwise AND operator compares each bit of the number with 1. If the last bit is 0, then the number is even. 
If the last bit is 1, then the number is odd."""
def is_even(num):
    if num&1==0:#if num is even
        return "EVEN"
    else:
        return "ODD"
num=int(input("Enter your number:"))
print(is_even(num))
#using Division
#This is a simple program to check whether a number is even or odd using division.
#If the number is divisible by 2, then it is even.
def check_even(num):
    if (num//2)*2==num:
        return "EVEN"
    else:
        return "ODD"
num=int(input("Enter your number:"))
#using a Lambda Function
#This is a simple program to check whether a number is even or odd using a lambda function.
#If the number is divisible by 2, then it is even.
#If the number is not divisible by 2, then it is odd.
is_even_odd=lambda num: "EVEN" if num%2==0 else "ODD"
num=int(input("Enter your number:"))
print(is_even_odd(num))
#Using a Dictionary
#This is a simple program to check whether a number is even or odd using a dictionary.
def is_even(num):
    return {True: "EVEN", False: "ODD"}[num%2==0]
num=int(input("Enter your number:"))
print(is_even(num))
#Using Ternary Operator
#A shorter conditional expression using Python's ternary operator.
def is_even(num):
    return "Even" if num%2==0 else "ODD"
num=int(input("Enter your number:"))
print(is_even(num))
#Using a List
def is_even(num):
    return ["EVEN","ODD"][num%2==0]
num=int(input("Enter your number:"))
print(is_even(num))
#Using divmod() function
#The divmod() function returns the quotient and remainder of the division.
def is_even(num):
    quotient,reminder=divmod(num,2)
    return "even" if reminder==0 else "odd"
num=int(input("Enter your number:"))
print(is_even(num))
#Using Recursion
def is_even(num):
    if num==0:
        return "EVEN"
    elif num==1:
        return "0DD"
    else:
        return is_even(num-2)
num=int(input("Enter your number:"))
print(is_even(num))

