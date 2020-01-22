#!/usr/bin/python

import argparse

def find_max_profit(prices):
  current_min_index = 0
  current_max_index = 0
  for i in range(1, len(prices)):
    print(f"iteration: {i}")
    if prices[i] < prices[current_min_index] and current_min_index <= i:
      current_min_index = i
    if prices[i] > prices[current_max_index] and current_min_index <= i:
      current_max_index = i
    print(f"current_min_index is now {current_min_index}, the price is {prices[current_min_index]}")
    print(f"current_max_index is now {current_max_index}, the price is {prices[current_max_index]}")      
  print(f"min: {prices[current_min_index]}, max: {prices[current_max_index]}")
  return prices[current_max_index] - prices[current_min_index]


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))