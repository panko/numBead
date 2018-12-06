def read_input():
    li = []
    n = int(input())
    for i in range(n):
        li.append(list(map(float, input().strip().split(' '))))
    return li

def norm1(li):
    return max([sum(list(map(abs, e))) for e in zip(*li)])

def main():
    li = read_input()
    print("%.12f" % round(norm1(li), 8))

if __name__ == '__main__':
    main()