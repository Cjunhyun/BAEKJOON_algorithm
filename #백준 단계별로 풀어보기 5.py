#백준 단계별로 풀어보기 5.문자열

# 27866번
w = input()
wlist = list(w)
n = int(input())
print(wlist[n-1])

# 2743번
w = input()
wlist = list(w)
print(len(wlist))

# 9086번
n = int(input())
for i in range(n):
    w = input()
    wlist=list(w)
    res = []
    res.append(wlist[0])
    res.append(wlist[len(wlist)-1])
    result = ''.join(str(s) for s in res)
    print(result)

# 11654번
n = input()
print(ord(n))

# 11720번
n = int(input())
num = input()
nums = list(num)
sum = 0
for i in nums:
    sum += int(i)
print(sum)

# 10809번
e = {'a':-1,'b':-1,'c':-1,'d':-1,'e':-1,'f':-1,'g':-1,'h':-1,'i':-1,'j':-1
     ,'k':-1,'l':-1,'m':-1,'n':-1,'o':-1,'p':-1,'q':-1,'r':-1,'s':-1,'t':-1,'u':-1,'v':-1
     ,'w':-1,'x':-1,'y':-1,'z':-1}

n = input()
ns = list(n)
for i in range(len(ns)):
    sv = ns[i]
    tmp = e[sv]
    if(tmp == -1):
        tmp = i
        e[sv] = tmp

res = []
for i in e:
    res.append(e[i])

result = ' '.join(str(s) for s in res)
print(result)

# 2675번
n = int(input())
for s in range(n):
    m = list(map(str,input().split()))
    x = m[0]
    y = list(m[1])
    res = []
    for i in range(len(y)):
        for j in range(int(x)):
            res.append(y[i])
    result = ''.join(str(s) for s in res)
    print (result)

# 1152번
n = input()
cnt = 1
k = list(n)
for i in k:
    if(i  == ' '):
        cnt += 1
if(k[0] == ' ' and k[len(k) - 1 ] == ' '):
    print(cnt - 2)
elif(k[0] == ' ' or k[len(k) - 1 ] == ' '):
    print(cnt - 1)
else:
    print(cnt)
