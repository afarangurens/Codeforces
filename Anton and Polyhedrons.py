from sys import stdin


def solve():
    s = {"T": 4, "C": 6, "O": 8, "D": 12, "I": 20}
    c = 0

    for i in range(int(stdin.readline())):
        c += s[stdin.readline().strip()[0]]
    print(c)


solve()