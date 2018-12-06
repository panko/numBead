#!/usr/bin/env python3

def read_input():
    A = []
    B = []
    k, m, n = map(int, input().strip().split(' ')) # 2
    for i in range(k):
        A.append(list(map(float, input().strip().split(' '))))
    for i in range(m):
        B.append(list(map(float, input().strip().split(' '))))
    return A, B

def mul_mat(A,B):
    R = [[0.0 for i in range(len(B[0]))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                R[i][j] += A[i][k] * B[k][j]

    return R 

def print_matrix(M):
    """Pretty prints matrix"""

    for i in range(len(M)):  
        for j in range(len(M[0])):  
            print("%.12f" % round(M[i][j], 12) ,end=" ")
        print("\n",end="") 

def main():
    A, B = read_input()
    print_matrix(mul_mat(A,B))

if __name__ == '__main__':
    main()