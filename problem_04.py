#!/usr/bin/env python

# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit
# numbers.

if __name__ == '__main__':
  max_palindrone = 0
  for a in range(0, 999):
    for b in range(0, 999):
      value = a * b
      if str(value) == str(value)[::-1] and value > max_palindrone:
        max_palindrone = value
  print(max_palindrone)