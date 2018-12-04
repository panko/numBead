#!/usr/bin/env python3

import numpy

def main():
    d = int(input())
    v = list(map(float, input().strip().split(' ')))
    w = list(map(float, input().strip().split(' ')))
    li = []

    for i in range(d):
        li.append( v[i] * w[i] )
    res = sum(li)

    print(res)
    print("%.12f" % res)
    print(round(res, 12) )
    print("%.12f" % round(res, 12))

if __name__ == '__main__':
    main()