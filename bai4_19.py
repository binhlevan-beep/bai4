def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False    
    for start in range(2, int(limit ** 0.5) + 1):
        if sieve[start]:
            for i in range(start * start, limit + 1, start):
                sieve[i] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]
limit = 1000000
prime_numbers = tuple(sieve_of_eratosthenes(limit))
print(prime_numbers)
