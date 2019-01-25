#!/usr/bin/env python

import functools
import math

@functools.lru_cache(maxsize=2048)
def triangle_number(n):
  if n < 1:
    raise Error('n must be > 0')
  elif n == 1:
    return 1
  else:
    return n + triangle_number(n - 1)

def divisors(n):
  subdiv_a = list(filter(lambda i: n % i == 0, range(1, math.ceil(math.sqrt(n)))))
  subdiv_b = list(map(lambda i: int(n / i), subdiv_a))
  return set(subdiv_a + subdiv_b + [ n ])

if __name__ == '__main__':
  n = 1
  n_triangle_number = triangle_number(n)
  n_divisors = divisors(n_triangle_number)
  while len(n_divisors) < 501:
    n += 1
    n_triangle_number = triangle_number(n)
    n_divisors = divisors(n_triangle_number)
  print('%d %d %d' % (n, n_triangle_number, len(n_divisors)))
