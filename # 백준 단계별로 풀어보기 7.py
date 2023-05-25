# 백준 단계별로 풀어보기 7
# 2738번
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
b = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        a[i][j] += b[i][j]

for i in a:
    print(*i)

#2566번
n_list = []
for i in range(9):
    n = list(map(int,input().split()))
    n_max = max(n)
    n_idx = n.index(n_max)

    n_tmp = []
    n_tmp.append(n_max)
    n_tmp.append(i+1)
    n_tmp.append(n_idx+1)

    n_list.append(n_tmp)

max_list = max(n_list)
print(max_list[0])
print(max_list[1], max_list[2])

#10798번
n_list = []
for i in range(15):
    n_list.append([])
for i in range(5):
    n = list(input())
    p = 0
    for j in n:
        n_list[p].append(j)
        p +=1
result = ''
for i in range(len(n_list)):
    res = ''.join(str(s) for s in n_list[i])
    result += res
    
print(result)

#2563번
n_list = [[0 for _ in range(101)] for _ in range(101)]
n = int(input())
for _ in range(n):
    x,y = list(map(int,input().split()))

    for r in range(x,x+10):
        for c in range(y, y+10):
            n_list[r][c] = 1
result = 0

for i in n_list:
    result += i.count(1)
print(result)