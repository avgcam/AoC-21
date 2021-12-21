import os
from collections import defaultdict, Counter, deque

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def load_data():
	file = 'sample21.txt'
	data = open(file).read().strip()
	return data

data = load_data()

'''
INPUT
'''
p1 = 10-1
p2 = 3-1

'''
SAMPLE
'''
#p1 = 4-1
#p2 = 8-1

die = 0

def roll():
  global die
  die += 1
  return die

s1 = 0
s2 = 0
while True:
  m1 = roll() + roll() + roll()
  p1 = (p1 + m1) % 10
  s1 += p1 + 1
  if s1 >= 1000:
    print(s2*die)
    break

  m2 = roll() + roll() + roll()
  p2 = (p2 + m2) % 10
  s2 += p2 + 1
  if s2 >= 1000:
    print(s1*die)
    break

'''
INPUT
'''
p1 = 10-1
p2 = 3-1

'''
SAMPLE
'''
#p1 = 4-1
#p2 = 8-1

DP = {}

def win(p1, p2, s1, s2):
  if s1 >= 21:
    return (1,0)
  if s2 >= 21:
    return (0, 1)
  if (p1, p2, s1, s2) in DP:
    return DP[(p1, p2, s1, s2)]
  ans = (0,0)
  for d1 in [1,2,3]:
    for d2 in [1,2,3]:
      for d3 in [1,2,3]:
        new_p1 = (p1+d1+d2+d3) % 10
        new_s1 = s1 + new_p1 + 1

        x1, y1 = win(p2, new_p1, s2, new_s1)
        ans = (ans[0] + y1, ans[1] + x1)
  DP[(p1, p2, s1, s2)] = ans
  return ans

print(max(win(p1, p2, 0, 0)))