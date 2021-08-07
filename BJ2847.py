## 백준알고리즘 2847번
## 게임을 만든 동준이

#입력
n = int(input())
n_list = []
for i in range(n):
    k =int(input())
    n_list.append(k)

#조건
cnt =0
k = n_list[n-1]
for i in range(n-1,-1,-1):
    if(n_list[i] > k):
        x = n_list[i] - k
        cnt += x
        k-=1
    elif(n_list[i] <= k):
        k = n_list[i]
        k-=1
    
  
#출력
print(cnt)
        
    