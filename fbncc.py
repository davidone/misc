#!/usr/bin/env python2


def fbncc(n):
    str = ""
    if n == 1:
        print "1"
        return
    if n == 2:
        print "1 1"
        return
    s = 1
    ss = 1
    str = "{:d} {:d}".format(s,s)
    for x in range(3, n+1):
      v = ss + s
      str = str + " {:d}".format(v)
      ss = s
      s = v
    print str
    return


if __name__ == "__main__":
    number = input("Insert a number: ")
    if int(number) != number:
        print "{:s} is not valid.".format(number)
        exit(1)
    fbncc(number)
