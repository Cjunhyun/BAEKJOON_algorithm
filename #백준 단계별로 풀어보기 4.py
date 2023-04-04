#백준 단계별로 풀어보기 4. 1차원배열

# 10807번
n = int(input())
c = list(map(int, input().split()))
k = int(input())

num =0
for i in range(len(c)):
    if(k == c[i]):
        num += 1
print(num)

# 10871번
n = list(map(int,input().split()))
num = list(map(int,input().split()))
ans = []
for i in range(len(num)):
    if(n[1]>num[i]):
        ans.append(num[i])
result = ' '.join(str(s) for s in ans)
print(result)

# 10818번
n = int(input())
num = list(map(int,input().split()))
print('%d %d' %(min(num), max(num)))
  
# 2562번
num = []
for i in range(9):
    n = int(input())
    num.append(n)

max = 0
maxi = 0

for i in range(9):
    if(max < num[i]):
        max = num[i]
        maxi = i+1
print(max)
print(maxi)

# 10810번
n,m = map(int,input().split())
blist = []
for i in range(n):
    blist.append(0)

for i in range(m):
    num = list(map(int,input().split()))
    for i in range(num[0],num[1]+1):
        blist[i-1] = num[2]
result = ' '.join(str(s) for s in blist)
print(result)

# 10813번
n,m = map(int,input().split())
blist = []
for i in range(n):
    blist.append(i+1)

for i in range(m):
    a,b = map(int,input().split())
    tem = blist[a-1]
    blist[a-1] = blist[b-1]
    blist[b-1] = tem
result = ' '.join(str(s) for s in blist)
print(result)

# 5597번
res = []
for i in range(1,31):
    res.append(i)

for i in range(28):
    n = int(input())
    res.remove(n)

for i in range(len(res)):
    print(res[i])

# 3052번
res = []
for i in range(10):
    n = int(input())
    k = n%42
    if(k not in res):
        res.append(k)
print(len(res))

# 10811번
n,m = map(int,input().split())
res = []
for i in range(n):
    res.append(i+1)

for i in range(m):
    a,b = map(int,input().split())
    tem = res[a-1:b]
    tem.reverse()
    res[a-1:b] = tem[0:len(tem)]
    
result = ' '.join(str(s) for s in res)
print(result)

# 1546번
n = int(input())
num = list(map(int,input().split()))
max_s = max(num)
sum = 0
for i in range(n):
        tem = num[i]/max_s*100
        sum += tem
print(sum/n)


