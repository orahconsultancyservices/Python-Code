"""
Problem: List all primes up to 290 using the Sieve of Eratosthenes.
"""

def primes_up_to(n=290):
    is_prime = [True] * (n + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, n + 1, i):
                is_prime[multiple] = False
    return [i for i, prime in enumerate(is_prime) if prime]


if __name__ == "__main__":
    result = primes_up_to()
    print(f"Primes up to 290:", result)
    print("Count:", len(result))
