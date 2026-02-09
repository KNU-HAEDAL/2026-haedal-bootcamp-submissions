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

def dfs():
    global map_list
    global obs_list
    global nmax
    
    if len(obs_list) == 3:
        nmax = max(sim(),nmax)

        return

        
    for i in range(col):
        for j in range(row):
            if map_list[j][i]==0:
                if len(obs_list) == 0:
                    obs_list.append([j,i])
                    map_list[j][i] = 1
                    dfs()
                    map_list[j][i] = 0
                    obs_list.pop()
                else:
                    if obs_list[-1][0]<j or (obs_list[-1][0]==j and obs_list[-1][1]<i):
                        obs_list.append([j,i])
                        map_list[j][i] = 1
                        dfs()
                        map_list[j][i] = 0
                        obs_list.pop()
                    

row, col = map(int, sys.stdin.readline().split())
map_list = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]

virus_list = []
obs_list = []
nmax = 0
for i in range(col):
    for j in range(row):
        if map_list[j][i]==2:
            virus_list.append([j, i])
dfs()

print(nmax)





        