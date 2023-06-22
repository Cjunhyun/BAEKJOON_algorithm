#백준단계별로 풀어보기 8

#2745번
# a,b = input().split(' ')
# a = ''.join(reversed(a))
# b = int(b)

# num = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# result = 0

# for i in range(len(a)-1,-1,-1):
#     sum = num.index(a[i]) * (b**i)
#     result += sum

# print(result)

a, b = input().rstrip().split()
print(int(a, int(b)))

#2720번
q = 25
d = 10
n = 5
p = 1

num = int(input())
for _ in range(num):
    charge = int(input())
    res = [0,0,0,0]
    while(charge > 0):
        if(charge >= 25): 
            res[0] = res[0]+1
            charge -= 25
        elif(charge >= 10):
            res[1] = res[1]+1
            charge -= 10
        elif(charge >= 5):
            res[2] = res[2]+1
            charge -= 5
        else:
            res[3] = res[3]+1
            charge -= 1
    
    print(*res)

# 2903번
print((2**int(input())+1)**2)

#2869번
a, b, v = map(int, input().split())

x = (v-b)/(a-b)
if x == int(x):
    print(int(x))
else:
    print(int(x) + 1)

#10757번
a,b = map(int, input().split())
print(a+b)