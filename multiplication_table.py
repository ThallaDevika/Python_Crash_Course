#Here are simple programs to print multiplication table
#USing print() function
n=int(input("Enter your number: "))
print("Multiplication table of", n, "is:")
print(n,"* 1 =", n*1)
print(n,"* 2 =", n*2)
print(n,"* 3 =", n*3)
print(n,"* 4 =", n*4)
print(n,"* 5 =", n*5)
print(n,"* 6 =", n*6)
print(n,"* 7 =", n*7)
print(n,"* 8 =", n*8)
print(n,"* 9 =", n*9)
print(n,"* 10 =", n*10)
# #Using for loop
n=int(input("Enter your number: "))
print("Multiplication table of ",n," is:")
for i in range(1,11):
    print(n,"*",i,"=",n*i)
    # #Using while loop
n=int(input("Enter your number: "))
print("Multiplication table of ",n," is:")
i=1
while i<=10:
    print(n,"*",i,"=",n*i)
    i+=1
# #Using function
def multiplication(n):
    print("Multiplication table of ",n,"is:")
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
n=int(input("Enter your number: "))
multiplication(n)
# #Using lambda function
n=int(input("Enter your number: "))
print("Multiplication table of ",n," is:")
multiplication_table=lambda n: [print (n,"*",i,"=",n*i) for i in range(1,11)]
multiplication_table(n)
# #Using list comprehension
n=int(input("Enter your number: "))
print("Multiplication table of ",n," is:")
multiplication_table=[print(n,"*",i,"=",n*i)for i in range(1,11)]
# #Using map function
n=int(input("Enter your number: "))
print("Multiplication table of ",n," is:")
multiplication_table=list(map(lambda i:print(n,"*",i,"=",n*i),range(1,11)))
# #Using filter function
n=int(input("Enter your number: "))
print("Multiplication table of ",n," is:")
multiplication_table=list(filter(lambda i:print(n,"*",i,"=",n*i),range(1,11)))
#using recursion
def multiplication_table(n,i=1):
    if i<=10:
        print(n,"*",i,"=",n*i)
        multiplication_table(n,i+1)
n=int(input("Enter your number: "))
print("Multiplication table of ",n," is:")
multiplication_table(n)
# #Using recursion with memoization
def multiplication_table(n,i=1,memo={}):
    if i in memo:
        return memo[i]
    if i<=10:
        memo[i]=n*i
        print(n,"*",i,"=",memo[i])
        multiplication_table(n,i+1,memo)
        
n=int(input("Enter your number: "))
print("Multiplication table of ",n," is:")
multiplication_table(n)
# #Using recursion with memoization and list comprehension
def multiplication_table(n,i=1,memo={}):
    if i in memo:
        return memo[i]
    if i<=10:
        memo[i]=n*i
        print(n,"*",i,"=",memo[i])
        multiplication_table(n,i+1,memo)
        n=int(input("Enter your number: "))
        print("Multiplication table of ",n," is:")
        multiplication_table(n)
n=int(input("Enter your number: "))
print("Multiplication table of ",n," is:")
multiplication_table(n)

# #Using functools.reduce
n=int(input("Enter your number: "))
print("Multiplication table of ",n," is:")
from functools import reduce
multiplication_table=reduce(lambda x,y:print(n,"*",x,"=",n*x),range(1,11))
# #Using numpy
import numpy as np
n=int(input("Enter your number: "))
print("Multiplication table of ",n," is:")
multiplication_table=np.arange(1,11)*n
print(multiplication_table)
# #Using pandas
import pandas as pd
n=int(input("Enter your number: "))
print("Multiplication table of ",n," is:")
multiplication_table=pd.Series(range(1,11))*n
print(multiplication_table)
# #Using scipy
import scipy
n=int(input("Enter your number: "))
print("Multiplication table of ",n," is:")
multiplication_table=scipy.arange(1,11)*n
print(multiplication_table)
# #Using matplotlib
import matplotlib.pyplot as plt
n=int(input("Enter your number: "))
print("Multiplication table of ",n," is:")
multiplication_table=plt.plot(range(1,11),[n*i for i in range(1,11)])
plt.xlabel("Multiplication")
plt.ylabel("Result")
plt.title("Multiplication table of "+str(n))
plt.show()
# #Using seaborn
import seaborn as sns
n=int(input("Enter your number: "))
print("Multiplication table of ",n," is:")
multiplication_table=sns.lineplot(x=range(1,11),y=[n*i for i in range(1,11)])
plt.xlabel("Multiplication")
plt.ylabel("Result")
plt.title("Multiplication table of "+str(n))
plt.show()
# #Using tkinter
import tkinter as tk
from tkinter import messagebox

n=int(input("Enter your number: "))
root = tk.Tk()
root.withdraw()  # Hide the root window
# #Using tkinter
# #Using tkinter messagebox
messagebox.showinfo("Multiplication table of "+str(n), "\n".join([str(n)+"*"+str(i)+"="+str(n*i) for i in range(1,11)]))
# #Using tkinter label
label = tk.Label(root, text="Multiplication table of "+str(n)+" is:")
label.pack()
for i in range(1,11):
    label = tk.Label(root, text=str(n)+"*"+str(i)+"="+str(n*i))
    label.pack()
root.mainloop()
# #Using tkinter entry
entry = tk.Entry(root)
entry.pack()
entry.insert(0, "Multiplication table of "+str(n)+" is:")
# #Using tkinter button
button = tk.Button(root, text="Show Multiplication table", command=lambda: messagebox.showinfo("Multiplication table of "+str(n), "\n".join([str(n)+"*"+str(i)+"="+str(n*i) for i in range(1,11)])))
button.pack()
root.mainloop()
# #Using tkinter canvas
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
canvas.create_text(200, 50, text="Multiplication table of "+str(n), font=("Arial", 20))
for i in range(1,11):
    canvas.create_text(200, 50+i*20, text=str(n)+"*"+str(i)+"="+str(n*i), font=("Arial", 15))
canvas.pack()
root.mainloop()


