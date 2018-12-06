#!/usr/bin/env python3

import math

def main():
    d = int(input())
    v = list(map(float, input().strip().split(' ')))
    w = list(map(float, input().strip().split(' ')))
    li = []

    for i in range(d):
        li.append( v[i] * w[i] )
    res = sum(li)

    print("%.12f" % round(res, 8))


if __name__ == '__main__':
    main()