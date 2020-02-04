#!/usr/bin/python

import sys

# 

# def rock_paper_scissors(n):
#   plays = []
#   for i in range(n):
#     print(i)
#     if n == 1:
#       print("hi")
#       plays.append(["rock"])
#       plays.append(["paper"])
#       plays.append(["scissors"])
#       return plays
#     plays.append(rock_paper_scissors(n-1))
#   return plays

def rock_paper_scissors(n):
  plays = []
  if n == 0:
    return [[]]
  if n == 1:
    plays.append(["rock"])
    plays.append(["paper"])
    plays.append(["scissors"])
    return plays
  for i in range(n-1):
    print(i)
    if len(plays) == 0:
      plays.append(["rock"])
      plays.append(["paper"])
      plays.append(["scissors"])
    temp_plays = []
    if n > 1:
      for j in range(len(plays)):
        print(f"Length of plays is {len(plays)}")
        print(f"Inner loop {j}")
        print(f"Appending {plays[j]} + ['rock']")
        temp_plays.append(plays[j] + ["rock"])
        temp_plays.append(plays[j] + ["paper"])
        temp_plays.append(plays[j] + ["scissors"])
        print(f"Current plays: {plays}")
        #plays.remove(plays[j])
      plays = temp_plays
    # plays.append(rock_paper_scissors(n-1))
  return plays



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')