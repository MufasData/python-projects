from sympy import isprime

def count_primes(number):
    
    prime_count = 0

    for i in range(number):
        if isprime(i) == True:
            prime_count += 1
            print(i)
        else:
            continue
    
    print(f"Number of prime number(s) between 0 and {number} are {prime_count}")

    return prime_count

num_needed = int(input("Input a number to find the number of prime numbers in between... "))

count_primes(num_needed)