def read_input():
    li = []
    n = int(input())
    for i in range(n):
        li.append(list(map(float, input().strip().split(' '))))
    return li

def norm_inf(li):
    return max([sum(list(map(abs, e))) for e in li])


def main():
    li = read_input()
    print("%.12f" % round(norm_inf(li), 8))

if __name__ == '__main__':
    main()