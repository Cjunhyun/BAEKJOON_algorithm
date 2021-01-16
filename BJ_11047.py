##백준 11047번

#동전 종류와 금액 입력(n,k)

n , k = map(int,input().split())

#각 동전의 금액을 리스트에 추가
n_list = []

for i in range(n):
    m = int(input())
    n_list.append(m)

#입력받은 동전의 금액을 오름차순으로 정렬
n_list = sorted(n_list)



#동전의 금액에 맞게 입력받은 금액을 내림차순으로 나누어 값을 구함
count = 0

for i in range(len(n_list)-1,-1,-1):
    if(n_list[i] <= k):
        x = k//n_list[i]
        count += x
        k = k % n_list[i]
    
print(count)
