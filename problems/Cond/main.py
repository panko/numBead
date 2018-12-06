#!/usr/bin/env python3

import numpy as np

from Matrix1Norma import norm1
from MatrixInfNorma import norm_inf

def main():
    A = read_input()
    np_A = np.array(A)
    print()
    A_inv = np.linalg.inv(np_A).tolist()
    asdA_inv = inv_mat(A)
    res_inf = norm_inf(A) *  norm_inf(A_inv)
    res_one = norm1(A) *  norm1(A_inv)
    print("%.12f %.12f" % (round(res_inf, 12), round(res_one, 12)) )

def read_input():
    A = []
    n = int(input())
    for i in range(n):
        A.append(list(map(float, input().strip().split(' '))))
    return A

def inv_mat(M):
    n = len(M)
    R = [[0.0 for i in range(n * 2 )] for j in range(n)]
    # copy my matrix
    for i in range(n):
        for j in range(n):
            R[i][j] = M[i][j]
    # place the identity matrix
    for i in range(n):
        for j in range(n, n * 2):
            if i == (j - n):
                R[i][j] = 1
    # do the inverse
    for i in range(n):
        t = R[i][i]
        for j in range(i, 2 * n):
            if t == 0:
                R[i][j] = 0.901
            else:
                R[i][j] = R[i][j] / t
        for j in range(n):
            if i != j:
                t = R[j][i]
                for k in range( 2 * n ):
                    R[j][k] -= t * R[i][k];
    # remove the identity
    for i in range(n * n):
            R[int(i / n)].pop(0)
    return R

if __name__ == '__main__':
    main()
