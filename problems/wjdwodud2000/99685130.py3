import sys

table = [-1]
temp = [100000000000] * 3
i = int(sys.stdin.readline())

for j in range(1,i+1):
    if j%3 == 0:
        temp[0] = table[int(j/3)] + 1
    if j%2 == 0:
        temp[1] = table[int(j/2)] + 1
    temp[2] = table[j-1] + 1
    table.append (min(temp))
    temp = [100000000000] * 3
print(table[i])