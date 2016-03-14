#!/usr/bin/env python2

'''
Generates automatically two arrays, a and b.
Return an arrays containing common elements in arrays
a and b.
'''

import random

SIZE_LIST_A = 10
SIZE_LIST_B = 20
a = []
b = []


def populate_arrays():
  for i in range(0, SIZE_LIST_A):
    a.append(random.randint(1, 100))
  for i in range(0, SIZE_LIST_B):
    b.append(random.randint(1, 100))

def return_list(a, b):
  c = []
  for i in a:
    if i in b and i not in c:
      c.append(i)
  return c


if __name__ == "__main__":
  populate_arrays()
  print "a: {:s}".format(str(a))
  print "b: {:s}".format(str(b))
  c = return_list(a, b)
  if len(c) > 0:
    print "c: {:s}".format(str(c))
  else:
    print "nothing in comon"

exit(0)
