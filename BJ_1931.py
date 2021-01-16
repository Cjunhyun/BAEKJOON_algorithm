##백준 1931번

#입력
n = int(input())
n_list = []
for i in range(n):
    start_t, end_t = map(int,input().split())

    n_list.append([])
    n_list[i].append(start_t)
    n_list[i].append(end_t)
#정렬
n_list = sorted(n_list)

#조건으로 출력

k_list = [[0,0]]

for i in range(n):
    m = len(k_list)-1

    a = n_list[i][0]
    b = n_list[i][1]

    c = k_list[m][0]
    d = k_list[m][1]

    if (c <= a and d > b ):
        k_list[m][0] = a
        k_list[m][1] = b

    elif (d <= a and d <= b ):
        k_list.append([])
        k_list[m+1].append(a)
        k_list[m+1].append(b)
    
    else:
        continue
print(k_list)
print(len(k_list)-1)