## 백준 2217번 로프

n = int(input())
k=[]
for i in range(n):
    kg = int(input())
    k.append(kg)

k = sorted(k)
c = 0
for i in range(n):
    x = k[i] * (n-i)

    if ( x > c):
        c = x

print (c)


