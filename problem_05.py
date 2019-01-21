#!/usr/bin/env python

# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by
# all of the numbers from 1 to 20?

VALUE_LIST = list(range(2, 21))

def evenly_divisible(n):
  return all(map(lambda i: n % i == 0, VALUE_LIST))

if __name__ == '__main__':
  n = 380
  found = False
  while not found:
    if evenly_divisible(n):
      print(n)
      found = True
    else:
      n += 380
