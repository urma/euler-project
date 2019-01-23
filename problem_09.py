#!/usr/bin/env python

# A Pythagorean triplet is a set of three natural numbers, a < b < c,
# for which, a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which
# a + b + c = 1000. Find the product abc.

def is_pythagorean_triplet(a, b, c):
  return (a < b) and (b < c) and (pow(a, 2) + pow(b, 2) == pow(c, 2))

if __name__ == '__main__':
  for a in range(1, 1000):
    for b in range(a, 1000):
        c = 1000 - a - b
        if is_pythagorean_triplet(a, b, c) and (a + b + c == 1000):
          print(a * b * c)