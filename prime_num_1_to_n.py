#  here are some simple programs that finds all the prime numbers between 1 and n.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def find_primes_up_to_n(n):
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes

# Input from the user
n = int(input("Enter the value of n: "))
prime_numbers = find_primes_up_to_n(n)

print(f"Prime numbers between 1 and {n} are:")
print(prime_numbers)


