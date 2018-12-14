#!/usr/bin/env python3

def readInput():
    li = []
    n = int(input())
    for i in range(n):
        li.append(list(map(float, input().strip().split(' '))))
    return li

def print_matrix(M):
    """Pretty prints matrix"""

    for i in range(len(M)):  
        for j in range(len(M[0])):  
            print("{:.12f}".format(M[i][j]), end=" ")
        print("\n",end="") 

def lu_decomposition(M):
    for i in range(len(M)):  
        for j in range(i+1, len(M)):
            Uresult = (M[j][i] / M[i][i])*-1
            for k in range(i, len(M)):
                M[j][k] = M[j][k] + (Uresult*M[i][k])
            M[j][i] = Uresult*-1
    return M

def main():
    matrix = readInput()
    try:
        M = lu_decomposition(matrix)
    except ZeroDivisionError as e:
        print("fail")
    else:
        print_matrix(M)
    
if __name__ == '__main__':
    main()
