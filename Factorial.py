#Here are simple programs to find the factorial of a number
#using for loop
num=int(input("Entter your number: "))
fact=1
for i in range(1,num+1):
    fact*=i
print("Factorial of", num, "is", fact)
# #using while loop
# num=int(input("Entter your number: "))
fact=1
i=1
while i<=num:
    fact*=i
    i+=1
print("Factorial of", num, "is", fact)
# #using recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
# num=int(input("Entter your number: "))
fact=factorial(num)
print("Factorial of", num, "is", fact)
# #using lambda function
# num=int(input("Entter your number: "))
fact=lambda n:1 if n==0 or n==1 else n*fact(n-1)
print("Factorial of", num, "is", fact(num))
# #using list comprehension
# num=int(input("Entter your number: "))
fact=[i for i in range(1,num+1)]
fact=1
for i in fact:
    fact*=i
print("Factorial of", num, "is", fact)
# #using map function
# num=int(input("Entter your number: "))
fact=list(map(int,range(1,num+1)))
fact=1
for i in fact:
    fact*=i
print("Factorial of", num, "is", fact)
# #using filter function
# num=int(input("Entter your number: "))
fact=list(filter(lambda x:x%2==0,range(1,num+1)))
fact=1
for i in fact:
    fact*=i
print("Factorial of", num, "is", fact)
# #using functools.reduce
# num=int(input("Entter your number: "))
fact=reduce(lambda x,y:x*y,range(1,num+1))
print("Factorial of", num, "is", fact)
# #using numpy
# import numpy as np
# num=int(input("Entter your number: "))
# fact=np.prod(np.arange(1,num+1))
# print("Factorial of", num, "is", fact)
# #using pandas
# import pandas as pd
# num=int(input("Entter your number: "))
# fact=pd.Series(range(1,num+1)).prod()
# print("Factorial of", num, "is", fact)
# #using scipy
# import scipy
# num=int(input("Entter your number: "))
# fact=scipy.prod(scipy.arange(1,num+1))
# print("Factorial of", num, "is", fact)
# #using math module
# import math
# num=int(input("Entter your number: "))
# fact=math.factorial(num)
# print("Factorial of", num, "is", fact)
# #using itertools
# import itertools
# num=int(input("Entter your number: "))
# fact=itertools.reduce(lambda x,y:x*y,range(1,num+1))
# print("Factorial of", num, "is", fact)
# #using sympy
import sympy
num=int(input("Entter your number: "))
fact=sympy.factorial(num)
print("Factorial of", num, "is", fact)
# #using sympy with memoization
# import sympy
# num=int(input("Entter your number: "))
# fact=sympy.factorial(num,memo=True)
# print("Factorial of", num, "is", fact)
# #using sympy with memoization and list comprehension
# import sympy
# num=int(input("Entter your number: "))
# fact=sympy.factorial(num,memo=True)
# fact=[i for i in range(1,num+1)]
# fact=1
# for i in fact:
#     fact*=i
# print("Factorial of", num, "is", fact)
# #using sympy with memoization and map function
# import sympy
# num=int(input("Entter your number: "))
# fact=sympy.factorial(num,memo=True)
# fact=list(map(int,range(1,num+1)))
# fact=1
# for i in fact:
#     fact*=i
# print("Factorial of", num, "is", fact)
# #using sympy with memoization and filter function

# import sympy
# num=int(input("Entter your number: "))
# fact=sympy.factorial(num,memo=True)
# fact=list(filter(lambda x:x%2==0,range(1,num+1)))
# fact=1
# for i in fact:
#     fact*=i
# print("Factorial of", num, "is", fact)
# #using sympy with memoization and functools.reduce
# import sympy
# num=int(input("Entter your number: "))
# fact=sympy.factorial(num,memo=True)
# fact=reduce(lambda x,y:x*y,range(1,num+1))
# print("Factorial of", num, "is", fact)

