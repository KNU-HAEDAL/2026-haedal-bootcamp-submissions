import sys
from collections import deque

col, row = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]

visited = [[0]*col for _ in range(row)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

success = True


dq = deque()
for i in range(row):
    for j in range(col):
        if graph[i][j] == 1:
            dq.append([j, i])
            y = i
            x = j

while dq:
    x,y = dq.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (nx>-1 and ny>-1 and nx<col and ny<row and graph[ny][nx]==0 and visited[ny][nx]==0):
            visited[ny][nx]=visited[y][x] + 1
            graph[ny][nx]=1
            dq.append([nx, ny])


for i in range(row):
    for j in range(col):
        if graph[i][j] == 0:
            success = False

if success == True:
    print(visited[y][x])
else:
    print(-1)
