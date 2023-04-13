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
