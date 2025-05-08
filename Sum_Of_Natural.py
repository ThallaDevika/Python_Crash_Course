#Here are some different ways to find the sum of natural numbers
#using for Loop
num=int(input("Enter your number: "))
sum=0
for i in range(1,num):
    sum+=i
    print("sum of", num, "natural numbers is",sum)
#using while Loop
num=int(input("Enter your number: "))
while(num>0):
    sum+=num
    num-=1
    print("sum of", num, "natural numbers is",sum)
#using recursion
def sum_of_natural_numbers(n):
    if n==0:
        return 0
    else:
        return n+sum_of_natural_numbers(n-1)
    num=int(input("Enter your number: "))
    print("sum of", num, "natural numbers is", sum_of_natural_numbers(num))
#using formula
num=int(input("Enter your number: "))
sum=(num*num+1)/2
print("sum of", num, "natural numbers is", sum)
#using lambda function
num=int(input("Enter your number: "))
sum=lambda num: num*(num)/2
print("sum of", num, "natural numbers is", sum(num))
#using list comprehension
num=int(input("Enter your number: "))
sum_=[i for i in range(1,num+1)]
sum_of_natural_numbers=sum(sum_)
print("sum of", num, "natural numbers is", sum_of_natural_numbers)
#using map function
num=int(input("Enter your number:"))
sum=list(map(int,range(1,num+1)))
sum_of_natural_numbers=sum(sum)
print("sum of", num, "natural numbers is", sum_of_natural_numbers)
#using filter function
num=int(input("Enter your number:"))
sum_=list(filter(lambda x: x%2>=0, range(1,num+1)))
sum_of_natural_numbers=sum(sum)
print("sum of", num, "natural numbers is", sum_of_natural_numbers)
#using functools.reduce
n=int(input())
from functools import reduce
sum=reduce(lambda x,y:x+y,range(1,n+1))
print("sum of", n, "natural numbers is", sum)
#using numpy
# #sum of natural numbers using for loop
sum=0
for i in range(1,num+1):
    sum+=i
    print("sum of", num, "natural numbers is", sum)
#sum of natural numbers using while loop
sum=0
num=int(input("Enter your number: "))
while num>0:
    sum+=num
    num-=1
    print("sum of", num, "natural numbers is", sum)
#sum of natural numbers using recursion
def sum_of_natural_numbers(n):
    if n==0:
        return 0
    else:
        return n+sum_of_natural_numbers(n-1)
num=int(input("Enter your number: "))
print("sum of", num, "natural numbers is", sum_of_natural_numbers(num))
#sum of natural numbers using formula
sum=(num*(num+1))/2
print("sum of", num, "natural numbers is", sum)
#sum of natural numbers using lambda function
sum=lambda num: num*(num+1)/2
print("sum of", num, "natural numbers is", sum(num))
#sum of natural numbers using list comprehension
sum_=[i for i in range(1,n+1)]
sum_of_natural_numbers=sum(sum_)
print("sum of", num, "natural numbers is", sum_of_natural_numbers)

#sum of natural numbers using map function
sum_=list(map(int,range(1,num+1)))
sum_of_natural_numbers=sum(sum_)
print("sum of", num, "natural numbers is", sum_of_natural_numbers)
#sum of natural numbers using filter function
sum_=list(filter(lambda x: x%2>=0, range(1,num+1)))
sum_of_natural_numbers=sum(sum_)
print("sum of", num, "natural numbers is", sum_of_natural_numbers)
#using dictionary comprehension
#sum of natural numbers using dictionary comprehension
sum_={i:i for i in range(1,num+1)}
sum_of_natural_numbers=sum(sum_.values())
print("sum of", num, "natural numbers is", sum_of_natural_numbers)
#sum of natural numbers using set comprehension

sum_={i for i in range(1,num+1)}
sum_of_natural_numbers=sum(sum_)
print("sum of", num, "natural numbers is", sum_of_natural_numbers)



