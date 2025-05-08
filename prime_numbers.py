#Here are some simple programs to find prime numbers in a given range
# #using for loop
num=int(input("Enter your number: "))
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def find_primes_range(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]
print(find_primes_range(10, 50))
#Sieve of Eratosthenes
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return [i for i in range(n + 1) if primes[i]]

print(sieve_of_eratosthenes(50))
#Segmented Sieve
def segmented_sieve(start, end):
    import math
    
    primes = sieve_of_eratosthenes(int(math.sqrt(end)))  # Find small primes first
    is_prime = [True] * (end - start + 1)

    for p in primes:
        start_idx = max(p*p, (start // p) * p)
        for j in range(start_idx, end + 1, p):
            is_prime[j - start] = False

    return [start + i for i in range(len(is_prime)) if is_prime[i]]

print(segmented_sieve(10, 50))
#Miller-Rabin Primality Test (Probabilistic)
import random

def miller_rabin(n, k=5):  
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    def check(a, d, n, r):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return True
        return False

    for _ in range(k):
        a = random.randint(2, n - 2)
        if not check(a, d, n, r):
            return False
    return True

print(miller_rabin(97))  # Checking if 97 is prime
#  Wheel Factorization (Optimized Trial Division)
def is_prime_wheel(n):
    if n < 2:
        return False
    if n in (2, 3, 5):
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False

    for i in range(7, int(n**0.5) + 1, 6):  # Skip unnecessary numbers
        if n % i == 0 or n % (i + 4) == 0:
            return False
    return True

print(is_prime_wheel(97))  # Checking if 97 is prime