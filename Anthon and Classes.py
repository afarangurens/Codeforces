from sys import stdin


def solve():
    maxl,minr = 0, 1000000001

    for i in range(int(stdin.readline())):
        l,r = map(int, stdin.readline().split())
        maxl = max(maxl, l)
        minr = min(minr, r)
    return maxl, minr


l1, r1 = solve()
l2, r2 = solve()

print(max(0,l2-r1, l1-r2))

