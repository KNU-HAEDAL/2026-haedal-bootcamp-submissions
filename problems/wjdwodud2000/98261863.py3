import sys
import copy
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def sim():
    cmax = 0
    sim_vistied_list = [[False]*col for _ in range(row)]
    sim_map_list=copy.deepcopy(map_list)
    sim_dq = deque()
    for virus in virus_list:
        sim_dq.append(virus)
    while sim_dq:
        [cy,cx]=sim_dq.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx>-1 and ny>-1 and col>nx and row>ny and sim_vistied_list[ny][nx] == False and sim_map_list[ny][nx]==0:
                sim_map_list[ny][nx] = 2
                sim_dq.append([ny, nx])
    for i in range(row):
       cmax+=sim_map_list[i].count(0) 
    return cmax

def dfs(wall_count, start):
    global nmax
    
    if wall_count == 3:
        nmax = max(sim(),nmax)
        return

        
    for i in range(start, row * col):
        r = i // col
        c = i % col
        
        if map_list[r][c]==0:
            map_list[r][c] = 1 
            dfs(wall_count + 1, i +1)
            map_list[r][c] = 0
                    

row, col = map(int, sys.stdin.readline().split())
map_list = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]

virus_list = []
nmax = 0
for r in range(row):
    for c in range(col):
        if map_list[r][c]==2:
            virus_list.append([r, c])
dfs(0,0)

print(nmax)