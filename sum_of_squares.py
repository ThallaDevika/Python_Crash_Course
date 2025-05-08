#Here are some other ways to find the sum of squares of natural numbers
# #using for Loop
num=int(input("Enter your number:"))
sum=0
for i in range(1,num+1):
    sum+=i*i
    print(sum)
# #using while Loop
while(num>0):
    sum+=num*num
    num-=1
    print(sum)
def sum_of_squares(n):
    if n==0:
        return 0
    else:
        return num*num+sum_of_squares(n-1)
    print(sum_of_squares(num))
# #using formula
# num=int(input("Enter your number:"))
sum=(num*(num+1)*(2*num+1))/6
print("sum of", num, "squares is", sum)
# #using lambda function
# num=int(input("Enter your number:"))
sum=lambda num:num*num*num+1*(2*num+1)/6
print("sum of", num, "squares is", sum(num))
# #using list comprehension
# num=int(input("Enter your number:"))
sum_=[i*i for i in range(1,num+1)]
sum=sum(sum+_)
print("sum of", num, "squares is", sum)
# #using map function
num=int(input("Enter your number:"))
sum=list(map(int,range(1,num+1)))
sum_of_squares=sum(sum_)
print("sum of", num, "squares is", sum_of_squares)
# #using filter function
num=int(input("Enter your number:"))
sum=list(filter(lambda x:x%2>=0,range(1,num+1)))
sum_of_squares=sum(sum_)
print("sum of", num, "squares is", sum_of_squares)
# #using functools.reduce
# n=int(input())
# from functools import reduce
# sum=reduce(lambda x,y:x+y*x,range(1,n+1))
# print(sum)
# #using numpy
# import numpy as np
# num=int(input("Enter your number:"))
# sum=np.sum(np.arange(1,num+1)**2)
# print("sum of", num, "squares is", sum)
# #using pandas
# import pandas as pd
# num=int(input("Enter your number:"))
# sum=pd.Series(range(1,num+1)).apply(lambda x:x**2).sum()
# print("sum of", num, "squares is", sum)
# #using scipy
# import scipy
# num=int(input("Enter your number:"))
# sum=scipy.sum(scipy.arange(1,num+1)**2)
# print("sum of", num, "squares is", sum)
# #using sympy
# import sympy
# num=int(input("Enter your number:"))
# sum=sympy.Sum(sympy.Symbol('x')**2,(sympy.Symbol('x'),1,num)).doit()
# print("sum of", num, "squares is", sum)
# #using math
import math
num=int(input("Enter your number:"))
sum=math.fsum([i*i for i in range(1,num+1)])
print("sum of", num, "squares is", sum)
# #using statistics
import statistics
num=int(input("Enter your number:"))
sum=statistics.fmean([i*i for i in range(1,num+1)])
print("sum of", num, "squares is", sum)
# #using random
import random
num=int(input("Enter your number:"))
sum=random.sample(range(1,num+1),num)
print("sum of", num, "squares is", sum)
# #using itertools
import itertools
num=int(input("Enter your number:"))
sum=itertools.accumulate(range(1,num+1),lambda x,y:x+y**2)
print("sum of", num, "squares is", sum)