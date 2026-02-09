import sys



N = int(sys.stdin.readline())
schedule_list=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

plan = []

max_reward = 0



def plan_finder(nday,new_reward):
    global max_reward
    if nday>=N:
        max_reward = max(max_reward, new_reward)      
        return
        
 
    if schedule_list[nday][0]+nday<N+1:
        plan_finder(schedule_list[nday][0]+nday,schedule_list[nday][1]+new_reward)
    plan_finder(nday+1,new_reward)
    

plan_finder(0,0)

print(max_reward)
    