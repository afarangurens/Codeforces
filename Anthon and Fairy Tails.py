from decimal import Decimal
from sys import stdin, stdout
from math import ceil


def solve_quadratic_formula(c):
    i = (-1 + Decimal(1 - 4 * c) ** Decimal(0.5)) / 2
    return ceil(i)


def solve():
    n, m = map(int, stdin.readline().split())
    # print(int(m+solve_quadratic_formula(n, m)))
    if m >= n:
        return n
    else:
        return m + solve_quadratic_formula(-2 * (n - m))


stdout.write(str(int(solve())))
