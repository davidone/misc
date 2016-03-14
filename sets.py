#!/usr/bin/env python2

'''
Generates automatically one array, a.
Prints an ordered list with only unique elems
'''

import random

SIZE_LIST_A = 10
a = []


def populate_arrays():
  for i in range(0, SIZE_LIST_A):
    a.append(random.randint(1, 100))


if __name__ == "__main__":
  populate_arrays()
  print "a: {:s}".format(str(a))
  b = list(set(a))
  b.sort()
  print "b: {:s}".format(str(b))

exit(0)
