#here are the different ways to count digits in a number
# # #using for loop
num=int(input("Enter your number:"))
count=0
for i in str(num):
    count+=1
print("Number of digits in", num, "is", count)
# # #using while loop
# num=int(input("Enter your number:"))
count=0
while num>0:
    count+=1
    num//10
print("Number of digits in", num, "is", count)
# # #using recursion
def count_digits(num):
    if num==0:
        return 0
    else:
        count+count_digits(num//10)
    return count+1
num=int(input("Enter your number:"))
count=count_digits(num)
print("Number of digits in", num, "is", count)
# # #using lambda function
num=int(input("Enter your number:"))
count=0
count=lambda num:1 if num==0 else count(num//10)+1
print("Number of digits in", num, "is", count(num))
# # #using list comprehension
# num=int(input("Enter your number:"))
count=[i for i in str(num)]
count(len(count))
print("Number of digits in", num, "is", count)
# # #using map function
num=int(input("Enter your number:"))
count=list(map(int,str(num)))
count=len(count)
print("Number of digits in", num, "is", count)
# # #using filter function
# num=int(input("Enter your number:"))
count=list(filter(lambda x:x%2==0,str(num)))
count=len(count)
print("Number of digits in", num, "is", count)
# # #using functools.reduce
# num=int(input("Enter your number:"))
count=reduce(lambda x,y:x+y,range(1,num+1))
print("Number of digits in", num, "is", count)
# # #using numpy
# import numpy as np
# num=int(input("Enter your number:"))
# count=np.count_nonzero(str(num))
# print("Number of digits in", num, "is", count)
# # #using pandas
# import pandas as pd
# num=int(input("Enter your number:"))
# count=pd.Series(str(num)).apply(lambda x:x.isdigit()).sum()
# print("Number of digits in", num, "is", count)
