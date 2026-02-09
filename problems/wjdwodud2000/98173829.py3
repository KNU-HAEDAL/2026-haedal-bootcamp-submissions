import sys

def cal():

    global max_num
    global min_num

    num = num_list[0]

    for i in range(n-1):
        if s[i] == 0:
            num = num + num_list[i+1]
        if s[i] == 1:
            num = num - num_list[i+1]
        if s[i] == 2:
            num = num * num_list[i+1]
        if s[i] == 3:
            num = int(num / num_list[i+1])



    if num>max_num:
            max_num = num
    if num<min_num:
            min_num = num



def dps():

    
    if len(s) == n-1:
        cal()
        return
    for i in range(4):
        if used_num[i]<opr_list[i]:
            s.append(i)
            used_num[i] = used_num[i]+1
            dps()
            s.pop()
            used_num[i] = used_num[i]-1
            
        


    


n = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))
opr_list = list(map(int,sys.stdin.readline().split()))

s = []

max_num = -1000000000
min_num = 1000000000



used_num = [0]*4 

dps()

print(max_num)
print(min_num)

