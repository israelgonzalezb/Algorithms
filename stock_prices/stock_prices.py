#!/usr/bin/python

import argparse

## This didn't work! lol
# def find_max_profit(prices):
#   current_min_index = 0
#   current_max_index = 1
#   current_min = prices[current_min_index]
#   current_max = 0
#   profit = current_max - current_min
#   for i in range(1, len(prices)):
#     print(f"iteration: {i}")
#     if prices[i] < prices[current_min_index] and current_min_index <= i and prices[current_max_index] > prices[current_min_index]:
#         print(f"  if {prices[i]} < {prices[current_min_index]} and {current_min_index} <= {i} and {prices[current_max_index]} >= {prices[current_min_index]}:")
#         current_min_index = i
#         print(f"    current_min_index is now {i}, the price is {prices[current_min_index]}")
#     if prices[i] > prices[current_max_index] and current_min_index <= i:
#       print(f"if {prices[i]} > {prices[current_max_index]} and {current_min_index} <= {i}:")
#       current_max_index = i
#       print(f"    current_max_index is now {i}, the price is {prices[current_max_index]}") 
#     current_min = prices[current_min_index]
#     current_max = prices[current_max_index]
#     profit = current_max - current_min
#     print(f"Profit: {profit}")     
#   print(f"min: {prices[current_min_index]}, max: {prices[current_max_index]}")
#   return prices[current_max_index] - prices[current_min_index]

def find_max_profit(prices):
  current_min_index = 0
  current_max_index = 0
  current_min = prices[current_min_index]
  current_max = prices[current_max_index]

  profit = prices[1] - prices[0] # initialize profit as the difference between the first two prices, always
  for i in range(1, len(prices)):
    current_number = prices[i]
    print(f"Current number: {current_number}")
    smallest_previous = 0
    for j in range(0, i):
      print(f"  Previous number: {prices[j]}")
      if j > 0 and prices[j-1] < prices[j]: # if the previous number is smaller than the current number
        smallest_previous = prices[j-1] # set it to be the smallest_previous number
      else: # otherwise
        smallest_previous = prices[j] # set the current number to be the smallest_previous number
      print(f"  The smallest previous number is: {smallest_previous}")
    if current_number - smallest_previous > profit:
      profit = current_number - smallest_previous
    print(f"The profit is: {profit}")
  return profit
  


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))