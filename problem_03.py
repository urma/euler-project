#!/usr/bin/env python

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

import math

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
  top_value = 600851475143
  n = math.ceil(math.sqrt(top_value))
  while not (top_value % n == 0 and is_prime(n)):
    n -= 1
  print(n)