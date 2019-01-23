#!/usr/bin/env python

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

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
  while n < 2000000:
    if is_prime(n):
      primes.append(n)
    n += 1
  print(sum(primes))