#백준 단계별로 풀어보기 9

#5086번
check = 1
while (check == 1):
    a,b = map(int,input().split())

    if(a == 0 and b == 0):
        check = 0
    
    elif(a <= b and b%a == 0):
        print("factor")
    elif ( a >= b and a%b == 0):
        print("multiple")
    else:
        print("neither")

#2501번
n,k = map(int,input().split())
n_list = []
for i in range(1,n+1):
    if(n%i == 0):
        n_list.append(i)

if(len(n_list) < k):
    print("0")
else:
    print(n_list[k-1])

#9506번
while(True):
    n = int(input())

    if(n == -1):
        break

    n_list = [] 
    n_sum = 0

    for i in range(1,n):
        if(n%i == 0 ):
            n_list.append(i)

    for k in n_list:
        n_sum += k
    
    if(n_sum == n):
        res = ' + '.join(str(s) for s in n_list)
        print(str(n) + ' = ' + res)
    else:
        print(str(n) + ' is NOT perfect.')