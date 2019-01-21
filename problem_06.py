#!/usr/bin/env python

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first
# ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

if __name__ == '__main__':
  values = list(range(1, 101))
  sum_squares = sum(map(lambda i: pow(i, 2), values))
  print(sum_squares)
  squares_sum = pow(sum(values), 2)
  print(squares_sum)
  print(squares_sum - sum_squares)