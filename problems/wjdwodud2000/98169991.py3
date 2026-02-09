import sys



def dps(num, max):
    if len(s) == max:
        print(*s)
        return
    for i in range(1, num+1):
        if s.count(i) == 0:
            s.append(i)
            dps(num, max)
            s.pop()


n, m = map(int, sys.stdin.readline().split())
s = []

dps(n, m)
