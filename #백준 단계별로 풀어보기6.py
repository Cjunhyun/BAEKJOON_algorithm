#백준 단계별로 풀어보기6
# 3003번
n_list = list(map(int,input().split()))
c = [1,1,2,2,2,8]
result = []

for i in range(len(n_list)):
    tem = c[i] - n_list[i]
    result.append(tem)

res = ' '.join(str(s) for s in result)
print(res)

# 2444번
n = int(input())

# 다이아몬드를 저장할 리스트 초기화
diamond = [" " * (2 * n - 1) for _ in range(2 * n - 1)]

# 다이아몬드 만들기
for i in range(n):
    diamond[i] = " " * (n - 1 - i) + "*" * (2 * i + 1)
    diamond[2 * n - 2 - i] = diamond[i]

# 다이아몬드 출력
for row in diamond:
    print(row)

# 10812번
n , m = map(int,input().split())
n_list = [] 
for i in range(1,n+1):
    n_list.append(i)

for i in range(m):
    i , j , k = map(int,input().split())
    i -= 1
    j -=1
    k -=1
    tem1 = n_list[i:k]
    tem2 = n_list[k:j+1]

    if(len(tem2) != 0 and len(tem1) != 0):

        n_list[i:i+len(tem2)] = tem2
        n_list[i+len(tem2):i+len(tem2)+len(tem1)] = tem1
    else:
        continue

res = ' '.join(str(s) for s in n_list)
print(res)