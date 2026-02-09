import sys
from collections import deque

def move(ry,rx,by,bx,direction):
    rnx, rny, bnx, bny = rx, ry, bx, by
    num_rball = 1
    num_bball = 1
    
    if direction == 0:
        if rx == bx:
            if ry<by:
                while map_list[rny-1][rnx] == ".":
                    rny -= 1
                if map_list[rny-1][rnx] == "O":
                    rny -= 1
                    num_rball = 0
                while map_list[bny-1][bnx] == "." and bny-1 != rny:
                    bny -= 1
                if map_list[bny-1][bnx] == "O":
                    num_bball = 0
                return rny,rnx,bny,bnx,num_rball,num_bball
            while map_list[bny-1][bnx] == ".":
                bny -= 1
            if map_list[bny-1][bnx] == "O":
                num_bball = 0
            while map_list[rny-1][rnx] == "." and bny != rny-1:
                rny -= 1
            if map_list[rny-1][rnx] == "O":
                rny -= 1
                num_rball = 0
            return rny,rnx,bny,bnx,num_rball,num_bball
                
        while map_list[bny-1][bnx] == ".":
            bny -= 1
        if map_list[bny-1][bnx] == "O":
            num_bball = 0
        while map_list[rny-1][rnx] == ".":
            rny -= 1
        if map_list[rny-1][rnx] == "O":
            rny -= 1
            num_rball = 0
        return rny,rnx,bny,bnx,num_rball,num_bball

    if direction == 1:
        if rx == bx:
            if ry>by:
                while map_list[rny+1][rnx] == ".":
                    rny += 1
                if map_list[rny+1][rnx] == "O":
                    rny += 1
                    num_rball = 0
                while map_list[bny+1][bnx] == "." and bny+1 != rny:
                    bny += 1
                if map_list[bny+1][bnx] == "O":
                    num_bball = 0
                return rny,rnx,bny,bnx,num_rball,num_bball
                
            while map_list[bny+1][bnx] == ".":
                bny += 1
            if map_list[bny+1][bnx] == "O":
                num_bball = 0
            while map_list[rny+1][rnx] == "." and bny != rny+1:
                rny += 1
            if map_list[rny+1][rnx] == "O" :
                rny += 1
                num_rball = 0
  
            return rny,rnx,bny,bnx,num_rball,num_bball
            
                
        while map_list[bny+1][bnx] == ".":
            bny += 1
        if map_list[bny+1][bnx] == "O":
            num_bball = 0
        while map_list[rny+1][rnx] == "." :
            rny += 1
        if map_list[rny+1][rnx] == "O":
            rny += 1
            num_rball = 0
        return rny,rnx,bny,bnx,num_rball,num_bball

    if direction == 2:
        if ry == by:
            if rx<bx:
                while map_list[rny][rnx-1] == ".":
                    rnx -= 1
                if map_list[rny][rnx-1] == "O":
                    rnx -= 1
                    num_rball = 0
                while map_list[bny][bnx-1] == "." and bnx-1 != rnx:
                    bnx -= 1
                if map_list[bny][bnx-1] == "O":
                    num_bball = 0
                return rny,rnx,bny,bnx,num_rball,num_bball
                
            while map_list[bny][bnx-1] == ".":
                bnx -= 1
            if map_list[bny][bnx-1] == "O":
                num_bball = 0
            while map_list[rny][rnx-1] == "." and bnx != rnx-1:
                rnx -= 1
            if map_list[rny][rnx-1] == "O":
                rnx -= 1
                num_rball = 0
            return rny,rnx,bny,bnx,num_rball,num_bball
      
                
        while map_list[bny][bnx-1] == ".":
            bnx -= 1
        if map_list[bny][bnx-1] == "O":
            num_bball = 0
        while map_list[rny][rnx-1] == ".":
            rnx -= 1
        if map_list[rny][rnx-1] == "O":
            rnx -= 1
            num_rball = 0
        return rny,rnx,bny,bnx,num_rball,num_bball

    if direction == 3:
        if ry == by:
            if rx>bx:
                while map_list[rny][rnx+1] == ".":
                    rnx += 1
                if map_list[rny][rnx+1] == "O":
                    rnx += 1
                    num_rball = 0
                while map_list[bny][bnx+1] == "." and bnx+1 != rnx:
                    bnx += 1
                if map_list[bny][bnx+1] == "O":
                    num_bball = 0
                return rny,rnx,bny,bnx,num_rball,num_bball

            while map_list[bny][bnx+1] == ".":
                bnx += 1
            if map_list[bny][bnx+1] == "O":
                num_bball = 0
            while map_list[rny][rnx+1] == "." and bnx != rnx+1:
                rnx += 1
            if map_list[rny][rnx+1] == "O":
                rnx += 1
                num_rball = 0
            return rny,rnx,bny,bnx,num_rball,num_bball
                
        while map_list[bny][bnx+1] == ".":
            bnx += 1
        if map_list[bny][bnx+1] == "O":
            num_bball = 0
        while map_list[rny][rnx+1] == ".":
            rnx += 1
        if map_list[rny][rnx+1] == "O":
            rnx += 1
            num_rball = 0
        return rny,rnx,bny,bnx,num_rball,num_bball
                    
  
N,M = map(int, sys.stdin.readline().split())
map_list = [list(sys.stdin.readline().rstrip()) for _ in range (N)]



rx = 0
ry = 0
bx = 0
by = 0



for row in range(N):
    for col in range(M):
        if map_list[row][col] == "R":
            ry, rx = row, col
            map_list[row][col] = "."
        if map_list[row][col] == "B":
            by, bx = row, col
            map_list[row][col] = "."
start_state = (ry, rx, by, bx, 0, 1)


result=-1
dq = deque([start_state])
visited=set()

    



while dq:
    current_ry, current_rx, current_by, current_bx, count, num_rball= dq.popleft()
    if num_rball==0:
        result=count
        break
    if count>10:
        count = -1
        break

    for i in range(4):
        new_ry, new_rx, new_by, new_bx, num_rball, num_bball = move(current_ry, current_rx, current_by, current_bx,i)
        if (new_ry, new_rx, new_by, new_bx) not in visited and num_bball == 1:
            visited.add((new_ry, new_rx, new_by, new_bx))
            dq.append((new_ry, new_rx, new_by, new_bx, count+1, num_rball))

print(result)