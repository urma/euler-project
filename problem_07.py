#!/usr/bin/env python

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def is_prime(n):
  # short-circuit
  if n <= 3:
    return n > 1
  elif (n % 2 == 0) or (n % 3 == 0):
    return False
  
  i = 5
  while i * i <= n:
    if (n % i == 0) or (n % (i + 2) == 0):
      return False
    i += 6
  return True

if __name__ == '__main__':
  n = 1
  primes = []
  while len(primes) < 10001:
    if is_prime(n):
      primes.append(n)
    n += 1
  print(primes[10000])