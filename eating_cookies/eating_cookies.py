#!/usr/bin/python

import sys
import timeit # library methods for timing how quickly a function is processed

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  # Thinking of dividing by each possible count... maybe using mod

  possible_ways = 0
  if n == 0:
    print("No more cookies!")
    return 1
  if n >= 1:
    print(f"{n} minus 1 is {n-1}")
    possible_ways += eating_cookies(n-1)
  if n >= 2:
    print(f"{n} minus 2 is {n-2}")
    possible_ways += eating_cookies(n-2)
  if n >= 3:
    print(f"{n} minus 3 is {n-3}")
    possible_ways += eating_cookies(n-3)
  # 1. He can eat 1 cookie at a time X times
  # If n > 0, then we'll always have at least one way to eat the cookies
  # 2. He can eat 1 cookie, then 2 cookies 
  print(possible_ways)
  return possible_ways

print(f"Time: {timeit.timeit('eating_cookies(3)', globals=globals(), number=1)}")

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')