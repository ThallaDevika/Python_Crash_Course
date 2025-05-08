# Method 1: Using a loop
def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i**2
    return total

# Method 2: Using a mathematical formula
def sum_of_squares_formula(n):
    return n * (n + 1) * (2 * n + 1) // 6

# Example usage
n = int(input("Enter a number: "))
print("Sum of squares (using loop):", sum_of_squares(n))
print("Sum of squares (using formula):", sum_of_squares_formula(n))
# Method 3: Using recursion
def sum_of_squares_recursive(n):
    if n == 1:
        return 1
    else:
        return n**2 + sum_of_squares_recursive(n - 1)
print("Sum of squares (using recursion):", sum_of_squares_recursive(n))
# Method 4: Using list comprehension
def sum_of_squares_list_comprehension(n):
    return sum(i**2 for i in range(1, n + 1))
print("Sum of squares (using list comprehension):", sum_of_squares_list_comprehension(n))
# Method 5: Using NumPy
import numpy as np
def sum_of_squares_numpy(n):
    return np.sum(np.arange(1, n + 1)**2)
print("Sum of squares (using NumPy):", sum_of_squares_numpy(n))
# Method 6: Using map and lambda
def sum_of_squares_map_lambda(n):
    return sum(map(lambda x: x**2, range(1, n + 1)))
print("Sum of squares (using map and lambda):", sum_of_squares_map_lambda(n))
# Method 7: Using filter and lambda
def sum_of_squares_filter_lambda(n):
    return sum(filter(lambda x: x % 2 == 0, map(lambda x: x**2, range(1, n + 1))))
print("Sum of squares (using filter and lambda):", sum_of_squares_filter_lambda(n))
# Method 8: Using functools.reduce
from functools import reduce
def sum_of_squares_reduce(n):
    return reduce(lambda x, y: x + y**2, range(1, n + 1), 0)
print("Sum of squares (using functools.reduce):", sum_of_squares_reduce(n))
# Method 9: Using a generator expression
def sum_of_squares_generator(n):
    return sum(i**2 for i in range(1, n + 1))
print("Sum of squares (using generator expression):", sum_of_squares_generator(n))
# Method 10: Using a while loop
def sum_of_squares_while(n):
    total = 0
    i = 1
    while i <= n:
        total += i**2
        i += 1
    return total
print("Sum of squares (using while loop):", sum_of_squares_while(n))
# Method 11: Using a list and sum
def sum_of_squares_list(n):
    squares = [i**2 for i in range(1, n + 1)]
    return sum(squares)
print("Sum of squares (using list and sum):", sum_of_squares_list(n))
# Method 12: Using a set and sum
def sum_of_squares_set(n):
    squares = {i**2 for i in range(1, n + 1)}
    return sum(squares)
print("Sum of squares (using set and sum):", sum_of_squares_set(n))
# Method 13: Using a dictionary and sum
def sum_of_squares_dict(n):
    squares = {i: i**2 for i in range(1, n + 1)}
    return sum(squares.values())
print("Sum of squares (using dictionary and sum):", sum_of_squares_dict(n))
# Method 14: Using a NumPy array
def sum_of_squares_numpy_array(n):
    arr = np.arange(1, n + 1)
    return np.sum(arr**2)
print("Sum of squares (using NumPy array):", sum_of_squares_numpy_array(n))
# Method 15: Using a NumPy matrix
def sum_of_squares_numpy_matrix(n):
    matrix = np.arange(1, n + 1).reshape(n, 1)
    return np.sum(matrix**2)
print("Sum of squares (using NumPy matrix):", sum_of_squares_numpy_matrix(n))
# Method 16: Using a NumPy tensor
def sum_of_squares_numpy_tensor(n):
    tensor = np.arange(1, n + 1).reshape(n, 1, 1)
    return np.sum(tensor**2)
print("Sum of squares (using NumPy tensor):", sum_of_squares_numpy_tensor(n))
# Method 17: Using a NumPy array with broadcasting
def sum_of_squares_numpy_broadcasting(n):
    arr = np.arange(1, n + 1).reshape(n, 1)
    return np.sum(arr**2, axis=0)
print("Sum of squares (using NumPy array with broadcasting):", sum_of_squares_numpy_broadcasting(n))
# Method 18: Using a NumPy array with a mask
def sum_of_squares_numpy_mask(n):
    arr = np.arange(1, n + 1)
    mask = arr % 2 == 0
    return np.sum(arr[mask]**2)
print("Sum of squares (using NumPy array with mask):", sum_of_squares_numpy_mask(n))
# Method 19: Using a NumPy array with a condition
def sum_of_squares_numpy_condition(n):
    arr = np.arange(1, n + 1)
    return np.sum(arr[arr % 2 == 0]**2)
print("Sum of squares (using NumPy array with condition):", sum_of_squares_numpy_condition(n))
# Method 20: Using a NumPy array with a filter
def sum_of_squares_numpy_filter(n):
    arr = np.arange(1, n + 1)
    return np.sum(arr[arr % 2 == 0]**2)
print("Sum of squares (using NumPy array with filter):", sum_of_squares_numpy_filter(n))
# Method 21: Using a NumPy array with a lambda function
def sum_of_squares_numpy_lambda(n):
    arr = np.arange(1, n + 1)
    return np.sum(np.array(list(map(lambda x: x**2, arr))))
print("Sum of squares (using NumPy array with lambda function):", sum_of_squares_numpy_lambda(n))
# Method 22: Using a NumPy array with a list comprehension
def sum_of_squares_numpy_list_comprehension(n):
    arr = np.arange(1, n + 1)
    return np.sum(np.array([x**2 for x in arr]))
print("Sum of squares (using NumPy array with list comprehension):", sum_of_squares_numpy_list_comprehension(n))
# Method 23: Using a NumPy array with a generator expression
def sum_of_squares_numpy_generator_expression(n):
    arr = np.arange(1, n + 1)
    return np.sum(np.array(i**2 for i in arr))
print("Sum of squares (using NumPy array with generator expression):", sum_of_squares_numpy_generator_expression(n))
# Method 24: Using a NumPy array with a for loop
def sum_of_squares_numpy_for_loop(n):
    arr = np.arange(1, n + 1)
    total = 0
    for i in arr:
        total += i**2
    return total
print("Sum of squares (using NumPy array with for loop):", sum_of_squares_numpy_for_loop(n))
# Method 25: Using a NumPy array with a while loop

def sum_of_squares_numpy_while_loop(n):
    arr = np.arange(1, n + 1)
    total = 0
    i = 0
    while i < len(arr):
        total += arr[i]**2
        i += 1
    return total
print("Sum of squares (using NumPy array with while loop):", sum_of_squares_numpy_while_loop(n))
# Method 26: Using a NumPy array with a do-while loop (simulated)
def sum_of_squares_numpy_do_while_loop(n):
    arr = np.arange(1, n + 1)
    total = 0
    i = 0
    while True:
        total += arr[i]**2
        i += 1
        if i >= len(arr):
            break
    return total
print("Sum of squares (using NumPy array with do-while loop):", sum_of_squares_numpy_do_while_loop(n))
# Method 27: Using a NumPy array with a for loop and a condition


